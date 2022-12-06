"""
TITLE: King Nerd Bot Main File
AUTHOR: SOVEREIGN SHAHID
DATE: 2022-09-24
"""
from discord import Option, Bot, ApplicationContext, Intents, Embed, ui
from dotenv import load_dotenv
import requests
import random
import json
import os
import datetime

load_dotenv()

with open("yo_mama_jokes.json") as f:
    jokes = json.load(f)



intents = Intents.default()
intents.message_content = True

bot = Bot(intents=intents)
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.listen()
async def on_message(message):
    global jokes
    if message.author == bot.user:
        return
    if "mom" in message.content.lower():
        await message.channel.send(jokes[random.randint(0,len(jokes)-1)])




@bot.slash_command(description="Repeats What you say",)
async def echo(
    ctx: ApplicationContext,
    phrase: Option(str, "Enter Phrase")
):
    await ctx.respond(f"{phrase}")


@bot.slash_command(description="Anonymous Confessions",)
async def confession(
    ctx: ApplicationContext,
    confession: Option(str, "Enter Confession")
):
    global bot
    confession_embed = Embed(title="Confession", description=confession)
    confession_channel = bot.get_channel(1044695496310132836)
    log_channel = bot.get_channel(1049512969022734437)
    log_embed = Embed(title="Confession log", description=f"{ctx.user} sent the following confession")
    log_embed.add_field(name="Timestamp", value=datetime.datetime.now())
    log_embed.add_field(name="Confession", value=confession)
    await log_channel.send(embed=log_embed)
    await confession_channel.send(embed=confession_embed)
    await ctx.send_response(content="Confession was sent sucessfully", ephemeral=True)

bot.run(os.getenv("BOT_TOKEN"))

# Hello Mommy
