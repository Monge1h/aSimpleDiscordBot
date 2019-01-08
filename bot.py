import discord
import asyncio
import random

from discord.ext import commands

TOKEN = 'Token'

answer = [
    "My reply is no.","My sources say no.",
    "Ask again later.","Ask again later.","Yes - definitely."
]


bot = commands.Bot(".")

@bot.event
async def on_ready():
    print("Bot Ready")
    #In this line you can change the game, to display en discord
    await bot.change_presence(game=discord.Game(name='Something'))
    

@bot.event
async def on_message(message):
    if message.content.startswith('.ping'):
        await bot.send_message(message.channel,'pong')
    #I use the random module to choice a random answers
    elif message.content.startswith('.8ball'):
        await bot.send_message(message.channel,random.choice(answer)) 
    
    
bot.run(TOKEN)