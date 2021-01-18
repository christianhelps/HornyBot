#!/usr/bin/env python3

# hornybot.py
# Python 3.6

import client_wrapper

def main():
    # The token from the 'Bot' tab, not the 'General Information' tab.
    keyfile = open('keys/discord-key', 'r') 
    TOKEN = keyfile.readline()
    
    bot = client_wrapper.ClientWrapper()
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
