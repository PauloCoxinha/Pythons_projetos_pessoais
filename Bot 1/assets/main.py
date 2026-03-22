import discord
from discord.ext import commands, tasks 
import os 
from dotenv import load_dotenv
from pathlib import Path
import datetime, pytz

#definimos o fusohorario e o horário para o bot mandar algo especifico
dt = datetime.datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
fuso_horario = dt.tzinfo
horario = datetime.time(20, 3, tzinfo=fuso_horario)

intents = discord.Intents.all()

#aqui dizemos que todo commando do bot vai ser com .
bot = commands.Bot(".", intents=intents)

env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("DISCORDIO_TOKEN")

try:
    if TOKEN:
        print("Tá funfando")
except:
    if TOKEN is None:
        raise ValueError("Token não encontrado no .env")




#Aqui inicia o bot e dps ele manda uma mensagem falando q iniciou
@bot.event
async def on_ready():
    enviar_mensagem.start()
    print("Bot inicializado bitch")
#ESSA FUNÇÃO FAZ COM QUE O BOT MANDE UMA MENSAGEM TODA VEZ Q VC DIGITAR .OLA
@bot.command()
async def ola(ctx):
    await ctx.reply("Ola! Tudo bem?")

@bot.command()
async def namorar(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Namorar com você? {nome} você quer ser humilhado agora ou depois? pobre imundo")

# @bot.event
# async def on_message(msg:discord.Message):
#     if msg.author.bot:
#         return
#     await msg.reply(f"O {msg.author.mention} Enviou uma mensagem no canal {msg.channel.name}")
#     await bot.process_commands(msg)

@bot.event
async def on_member_join(member:discord.Member):
    canal = bot.get_channel(1415696880138195036)
    await canal.send(f"Bem vindo {member.mention}!")

@bot.event 
async def on_reaction_add(reacao:discord.Reaction, member:discord.Member):
    await reacao.message.reply(f"O membro {member.name} Reagiu a essa mensagem com essa reação: {reacao.emoji}")

@bot.command()
async def somar(ctx:commands.Context, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"A soma entre os números digitados é: {resultado}")

@tasks.loop(time=horario)
async def enviar_mensagem():
    canal = bot.get_channel(1415696880138195036)  
    await canal.send(f"Oi, por acaso sua mãe sabe q vc gosta de rapazes?")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "Titulo mt criativo pra quem n tem nada"
    minha_embed.description = "Minha descrição superior"


    caminho_base = os.path.dirname(__file__ )
    caminho_imagem = os.path.join(caminho_base, "img", "72.jpg")
    imagem = discord.File(caminho_imagem, "Safada.jpg")

    minha_embed.set_image(url="attachment://Safada.jpg" )

    await ctx.reply(embed=minha_embed, file=imagem)



         


bot.run(TOKEN) 