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


def add_gif_to_db(message, command):
    json_request = {
        "catagory": command,
        "url": message.content.split(' ')[2],
        "addedBy": message.author.name
    }
    
    print(json_request)
    requests.post(url = "http://10.0.0.29:3000/gifs", data = json_request) 


def gif_add(message, command):
    if "add" == message.content.split(' ')[1]:
        add_gif_to_db(message, command)
        return True
    else:
        return False


def get_db_gif_url(command):
    response = requests.get(url = "http://10.0.0.29:3000/gifs",
        params = { "catagory": command }
        )
    data = response.json()
    return random.choice(data)['url']


async def handle_gif_embed(message, command):
    if gif_add(message, command):
        return

    if 0 == len(message.mentions):
        err_embed = discord.Embed()
        err_embed.description = "Must ping a user to " + command + ", or provide a URL with 'add [URL]'"
        await message.channel.send(embed=err_embed)
        return 

    gif_embed = discord.Embed(colour = discord.Color.blue())

    gif_url=get_db_gif_url(command)
    gif_embed.set_image(url = gif_url)

    gif_embed.title = ""
    gif_embed.description = '{0.author.mention} '.format(message) + command + 's {0.mentions[0].mention}'.format(message)

    await message.channel.send(embed=gif_embed)
    return


async def spank(message):
    await handle_gif_embed(message, "spank")


async def kiss(message):
    await handle_gif_embed(message, "kiss")
