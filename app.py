from email.message import Message
from http.client import responses
import nextcord
from nextcord.ext import commands
import os
import asyncio
import requests, json, random, datetime

responses = json.load(open("responses.json"))

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)
bot.remove_command('help')

@bot.command(name="hello", description="ppang will say hi to you")
async def sayHi(ctx):
    await ctx.send(random.choice(responses["hello"]))
    
@bot.command(name="bread", description="sends you bread")
async def bread(ctx):
    await ctx.send('🍞')
    
@bot.command(name="moyai", description="judges you")
async def bread(ctx):
    await ctx.send('🗿')
    
@bot.command(name="313")
async def beomgyu(ctx):
    await ctx.send(random.choice(responses["beomgyu"]))
    
@bot.command(name="doggo", description="sends a random dog pic")
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    link2img = response.json()["message"]
    await ctx.send(link2img)
    
@bot.command(name="cat", description="sends a random cat pic")
async def cat(ctx):
    link2img = json.loads(requests.get('http://aws.random.cat/meow').content)["file"]
    await ctx.send(link2img)
    
@bot.command(name="morb", description="its morbin time")
async def morb(ctx):
    await ctx.send("it's morbin time!\n")
    await ctx.send("https://i.pinimg.com/originals/40/1a/57/401a577ead6776c2101d0f78acd90681.gif")
    
@bot.command(name="pun", description="sends a neat pun")
async def bread(ctx):
    response = requests.get("https://my-bao-server.herokuapp.com/api/breadpuns")
    await ctx.send(response.text[1:-1])
    
@bot.command(name="anime", description="recommends a random anime")
async def anime(ctx):
    response = requests.get("https://api.jikan.moe/v4/random/anime")
    await ctx.send(response.json()["data"]["title"])
    await ctx.send(response.json()["data"]["images"]["jpg"]["image_url"])
    
@bot.command(name="ppangtan", description="sends an inspirational bts quote")
async def bbangtan(ctx):
    response = requests.get('https://bts-quotes-api.herokuapp.com/quote/random')
    quote = response.json()["quote"]
    member = response.json()["member"]
    await ctx.send('*{}*\n-{}'.format(quote, member))
    
@bot.command(name="genshin", description="rolls a random genshin character")
async def genshin(ctx):
    response = requests.get('https://genshin-app-api.herokuapp.com/api/characters?infoDataSize=[all/minimal]')
    characters = response.json()["payload"]["characters"]
    character = random.choice(characters)
    await ctx.send(character["name"])
    await ctx.send(character["cardImageURL"])
    
    
@bot.command(description="help command for ppangBot")
async def help(ctx):
    embed = nextcord.Embed(title='ppangBot commands 🍞', description="help command for ppangBot")
    for command in bot.walk_commands():
        description = command.description
        if not description or description is None or description == "":
            description = "its a mystery!"
        embed.add_field(name=f"'?{command.name}{command.signature if command.signature is not None else ''}'", value=description)
    await ctx.send(embed=embed)
    
@bot.command(name="hug", description="give someone a hug")
async def hug(ctx, *receiver):
    if receiver is None or not receiver or len(ctx.message.raw_mentions) != 1 or len(receiver) != 1:
        raise commands.BadArgument()
    await ctx.send(f"hiya <@{ctx.message.raw_mentions[0]}>, user {ctx.message.author.name} just sent you a hug! <3")
    
    
@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Incorrect format. The command should be formatted in this way: `?hug @user`.""")
    
    
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))