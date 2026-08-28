# 🛍️ Shopee Deals Bot

Bot em Python que busca ofertas de produtos de tecnologia na **Shopee** (via API de afiliados) e posta automaticamente as melhores promoções em um canal/grupo do **Telegram**.

## ✨ Funcionalidades

- Busca produtos na Shopee usando a API GraphQL de afiliados (`productOfferV2`)
- Sorteia palavras-chave de uma lista de categorias de hardware/PC (teclado, mouse, monitor, placa de vídeo, etc.)
- Filtra apenas produtos válidos: com preço, com desconto e com pelo menos 5 vendas
- Posta no Telegram com foto, preço, desconto, avaliação, quantidade de vendas e link de compra
- Loop contínuo, buscando novas ofertas periodicamente
- Persistência em SQLite para controlar produtos já postados

## 📦 Pré-requisitos

- Python 3.9+
- Conta no [Programa de Afiliados da Shopee](https://affiliate.shopee.com.br/) com `App ID` e `Secret`
- Um bot do Telegram (criado via [@BotFather](https://t.me/BotFather)) e o `chat_id` do canal/grupo de destino

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
```

### Dependências

```
requests
python-dotenv
python-telegram-bot
```

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
APP_ID=seu_app_id_shopee
SECRET=seu_secret_shopee
TELEGRAM_TOKEN=seu_token_do_bot_telegram
CHAT_ID=id_do_chat_ou_canal
```

> ⚠️ Nunca versione o arquivo `.env`. Adicione-o ao `.gitignore`.

## ▶️ Uso

```bash
python bot.py
```

O bot irá:
1. Escolher uma palavra-chave aleatória entre as categorias configuradas
2. Buscar ofertas na Shopee
3. Filtrar produtos válidos e ainda não postados
4. Publicar a primeira oferta válida no Telegram
5. Aguardar antes de repetir o ciclo

## 🛠️ Personalização

- **Categorias de busca**: edite a lista `KEYWORDS` no início do script
- **Intervalo entre postagens**: ajuste o valor em `asyncio.sleep(...)` dentro da função `main()`
- **Critérios de filtro** (preço mínimo, vendas mínimas etc.): ajuste as condições dentro do loop `produtos_validos`

## 🗃️ Banco de dados

O projeto usa SQLite (`banco.db`) para registrar produtos já postados e evitar repetições.

> ⚠️ **Atenção:** as funções `salvar_produto` e `ja_foi_postado` estão implementadas, mas atualmente o controle de duplicados no `main()` usa apenas um `set()` em memória (`produtos_já_postados`), que é reiniciado toda vez que o bot é reiniciado. Há também um erro de sintaxe no `INSERT` de `salvar_produto` (parêntese faltando) que impede a gravação no banco. Vale revisar antes de depender da persistência entre execuções.

