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

        # Don't process a message without the prefix.
        if not message.content.startswith('!'):
            return

        # Strip the first word of the message and call the matching command function.
        await getattr(commands, message.content.split()[0][1:], commands.invalid_command)(message)


    @client.event
    async def on_ready():
        print('HornyBot is live.')
        print("ID: " + str(ClientWrapper.client.user.id))
    

    def run(self, token):
        self.client.run(token)
