import discord
from discord.ext import commands, tasks 
import os 
from dotenv import load_dotenv
from pathlib import Path
from datetime import time 

env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("DISCORDIO_TOKEN")

if TOKEN is None:
    raise ValueError("Token não encontrado no .env")

print("Variáveis carregadas:", os.environ)
print("TOKEN:", os.getenv("DISCORDIO_TOKEN")) 

print(f"TOKEN RAW:", repr(TOKEN))

print(f"token : {TOKEN}")

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)


@bot.event
async def on_ready():
    enviar_mensagem.start()
    print("Bot inicializado bitch")

@bot.command()
async def ola(ctx):
    await ctx.reply("Ola! Tudo bem?")

@bot.command()
async def namorar(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Namorar com você? {nome} você quer ser humilhado agora ou depois? pobre imundo")

@bot.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    await msg.reply(f"O {msg.author.mention} Enviou uma mensagem no canal {msg.channel.name}")
    await bot.process_commands(msg)

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

@tasks.loop(seconds=10)
async def enviar_mensagem():

bot.run(TOKEN) 