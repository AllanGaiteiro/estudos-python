import discord
import random
import math

bot = discord.Client()
token = 'www'
config = {
    "prefix":"y!"
}


bot.login(token)

bot.on('message', message())

def message(msg):
    if msg.content == 'Decisão':
        msg.reply(((random())))
