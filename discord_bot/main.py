import discord
from discord.ext import commands
from bot_logic import dice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ayuda(ctx):
    await ctx.send("Hola soy un bot hecho en clases de Kodland \n puedes usar estos comandos: ")
    await ctx.send("$dado [lados] [numero de dados] \n$heh [numero de veces para repetir 'heh'] \n$hello")
    

@bot.command()
async def dado(ctx, sides = 6, count = 2):
    await ctx.send(dice(sides, count))

bot.run("token")
