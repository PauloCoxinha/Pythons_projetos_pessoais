import hashlib
import time
import json
import requests
import os
import asyncio
from dotenv import load_dotenv
import telegram
import random 
import sqlite3






# Carrega as credenciais do .env
load_dotenv()
APP_ID= os.getenv("APP_ID")
SECRET= os.getenv("SECRET")
TELEGRAM_TOKEN= os.getenv("TELEGRAM_TOKEN")
CHAT_ID= os.getenv("CHAT_ID")

BASE_URL = "https://open-api.affiliate.shopee.com.br/graphql"

KEYWORDS = [
    "Teclado mecânico",
    "Pc gamer",
    "Mouse",
    "Monitor",
    "Placa de video",
    "Processador",
    "Gabinete",
    "Fonte",
    "Memoria RAM",
    "SSD"
]

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto text NOT NULL)


""")
conexao.commit()

def ja_foi_postado(nome_produto: str) -> bool:
    cursor.execute("SELECT 1 FROM produtos WHERE Nome_Produto = ?", (nome_produto,)) 
    return cursor.fetchone() is not None

def salvar_produto(nome_produto:str):
    try:
        cursor.execute("INSERT INTO produtos (Nome_Produto VALUES (?)", (nome_produto,))
        conexao.commit()

    except sqlite3.IntegrityError:
        print("Produto já cadastrado")

# ── Shopee ────────────────────────────────────────────────
def gerar_headers(payload: dict) -> dict:
    timestamp = str(int(time.time()))
    body_str  = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
    raw       = APP_ID + timestamp + body_str + SECRET
    signature = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    return {
        "Content-Type": "application/json",
        "Authorization": f"SHA256 Credential={APP_ID}, Timestamp={timestamp}, Signature={signature}"
    }

def buscar_roupas(limite=200):
     keyword = random.choice(KEYWORDS)  # escolhe uma keyword aleatória
     print(f"🔍 Buscando por: {keyword}")
    
     query = '{ productOfferV2(keyword: "' + keyword + '", listType: 1, sortType: 5, limit: ' + str(limite) + ') { nodes { productName offerLink imageUrl priceMin priceDiscountRate commissionRate ratingStar sales } } }'
     payload = {"query": query}

     timestamp = str(int(time.time()))
     body_str  = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
     raw       = APP_ID + timestamp + body_str + SECRET
     signature = hashlib.sha256(raw.encode('utf-8')).hexdigest()

     headers = {
        "Content-Type": "application/json",
        "Authorization": f"SHA256 Credential={APP_ID}, Timestamp={timestamp}, Signature={signature}"
    }

     response = requests.post(BASE_URL, data=body_str.encode('utf-8'), headers=headers)
     return response.json()

# ── Telegram ──────────────────────────────────────────────
async def postar_produto(produto: dict):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    preco     = float(produto["priceMin"] or 0)
    desconto  = produto["priceDiscountRate"] or 0
    comissao  = float(produto["commissionRate"] or 0) * 100
    nome      = produto["productName"]
    link      = produto["offerLink"]
    imagem    = produto["imageUrl"]
    avaliacao = produto["ratingStar"] or 0
    vendidos  = produto["sales"] or 0

    texto = (
        f"🛍️ *{nome}*\n\n"
        f"💰 Por apenas *R$ {preco:.2f}*\n"
        f"🔥 *{desconto}% de desconto!*\n"
        f"⭐ Avaliação: {avaliacao} | 📦 {vendidos} vendidos\n\n"
        f"👉 [Compre aqui]({link})"
    )

    await bot.send_photo(
        chat_id=CHAT_ID,
        photo=imagem,
        caption=texto,
        parse_mode="Markdown"
    )
    print(f"✅ Postado: {nome}")

async def main():
    produtos_já_postados = set()

    while True:
        print("🔍 Buscando roupas na Shopee...")
        resultado = buscar_roupas(limite=50)

        if "errors" in resultado:
            print("❌ Erro na API Shopee:", resultado["errors"])
        else:
            produtos = resultado["data"]["productOfferV2"]["nodes"]

            produtos_validos = [
                p for p in produtos
                if p["priceMin"] and p["priceDiscountRate"]
                and float(p["priceMin"]) > 0
                and float(p["priceDiscountRate"]) > 0
                and int(p["sales"] or 0) >= 5
                and p["productName"] not in produtos_já_postados
            ]

            print(f"✅ {len(produtos_validos)} produtos válidos encontrados!")

            if produtos_validos:
                produto = produtos_validos[0]
                await postar_produto(produto)
                produtos_já_postados.add(produto["productName"])
            else:
                print("⚠️ Nenhum produto novo encontrado!")

        print("⏳ Aguardando 5 minutos...")
        await asyncio.sleep(10)

asyncio.run(main())