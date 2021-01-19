# commands.py
# Python 3.6

import asyncio
import discord
import random
# HTTP requests.
import requests
# Server load data.
import psutil
import datetime

STARTUP_TIME = datetime.datetime.now()

async def invalid_command(message):
    await message.channel.send("Invalid command.")


async def hello(message):
    await message.channel.send('Hello {0.author.mention}'.format(message))


async def help(message):
    command_list = ["hello", "help", "spank"]
    await message.channel.send("Commands: " + ', '.join(command_list))


async def spank(message):
    keyfile = open('keys/google-key', 'r') 
    GOOGLE_TOKEN = keyfile.readline()[:-1]

    engine_file = open('keys/search-id', 'r') 
    ENGINE_ID = engine_file.readline()[:-1]

    json_request = {
        "key": GOOGLE_TOKEN,
        "cx": ENGINE_ID,
        "q": "bondage spanking gif"
    }
        #"domain": "google.com",

    response = requests.get(url = "https://www.googleapis.com/customsearch/v1", params = json_request) 
    retriever_data = response.json()

    #"api_key": os.getenv("GOOGLE_TOKEN")

    retriever_embed = discord.Embed(colour = discord.Color.blue())
    retriever_embed.title = "Spank!"
    retriever_embed.description = '{0.author.mention} spanks {0.mentions[0].mention}'.format(message)
    # retriever_embed.description = str(retriever_data['items'][random.randint(0,9)]['pagemap']['cse_image'][0]['src'])
    # list from 0-99, shuffle the list, and the access the indicies in a for loop.
    for data in retriever_data['items'][random.randint(0,9)]['pagemap']:
    
    # gif_url = str(retriever_data['items'][random.randint(0,9)]['pagemap']['cse_image'][0]['src'])
    retriever_embed.set_image(url = gif_url)

    await message.channel.send(embed=retriever_embed)
