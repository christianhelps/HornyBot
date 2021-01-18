# client_wrapper.py
# Python 3.6

import asyncio
import discord

import commands

class ClientWrapper:

    client = discord.Client()

    def __init__(self):
        pass
    
    @client.event
    async def on_message(message):
        # We don't want the bot to process its own messages.
        if message.author == ClientWrapper.client.user:
            return

        await commands.process_user_command(message)


    @client.event
    async def on_ready():
        print('HornyBot is live.')
        print("ID: " + str(ClientWrapper.client.user.id))
    

    def run(self, token):
        self.client.run(token)
