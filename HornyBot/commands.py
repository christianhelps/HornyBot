# commands.py
# Python 3.6

import asyncio
import discord
import random
import requests
import psutil
import datetime

STARTUP_TIME = datetime.datetime.now()

def get_commands():
    return ["hello", "help", "healthcheck"]

            
def get_current_weather_embed(request):
    keyfile = open('keys/weather-key', 'r') 
    WEATHER_TOKEN = keyfile.readline()
    
    zipcode = request.split(' ')[1]
    response = requests.get(url = "http://api.weatherapi.com/v1/current.json",
                            params = {'q': zipcode, 'key': WEATHER_TOKEN})
    weather_data = response.json()
    print(weather_data)

    # Messy string formatting to build our object to embed.
    emb = discord.Embed(colour = discord.Color.blue())
    emb.title = str(weather_data['location']['name']) + ", " + str(weather_data['location']['region']) 
    emb.description = str(weather_data['current']['condition']['text']) + " and " \
        + str(weather_data['current']['temp_f']) + "f with " \
        + str(weather_data['current']['wind_mph']) + "mph of wind."
    emb.set_image(url = "http://" + str(weather_data['current']['condition']['icon'])[2:])
    
    return emb

            
def get_health_embed():
    cpu_val = psutil.cpu_percent()
    ram_val = psutil.virtual_memory().percent

    emb = discord.Embed(colour = discord.Color.green())
    emb.title = str("System status: Nominal")
    emb.description = "GoodBot instance has been live for " + str(datetime.datetime.now() - STARTUP_TIME ) \
        + " \n Current server load: CPU Usage - " \
        + str(cpu_val) + "%, RAM Usage - " + str(ram_val) + "%."
    emb.set_image(url = "https://media3.giphy.com/media/JRmilld9HS2CjW0miL/giphy.gif")
    
    return emb

            
def process_simple_command(message):
    if message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        return msg

    
    if message.content.startswith('?help'):
        return "!hello,!help, !healthcheck"

    return ""


async def process_user_command(message):
    # Don't process messages that don't have the prefix
    if not message.content.startswith('!'):
        return
    
    # Return quickly if the command doesn't match a known command.
    if not message.content.split()[0][1:] in get_commands():
        await message.channel.send("Invalid command.")
        return
        
    if message.content.startswith('?healthcheck'):
        health_embed = get_health_embed()
        await message.channel.send(embed=health_embed)
    
    out_message = process_simple_command(message)
    if out_message != "":
        await message.channel.send(out_message)
