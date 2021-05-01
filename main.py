import os
import discord
from server import keep_alive
import random
import basic_utilities, advice, poems, biography, usage

client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    if message.author != client.user:

        # Insult Command
        if message.content.startswith("!insult"):
            if (message.content != "!insult"):
                target = message.content.split(" ")[1]
                await message.channel.send(
                    random.choice(basic_utilities.roasts) + target)
            else:
                await message.channel.send(
                    "Usage: !insult [name of person you wanna roast]")

        # Advice Command
        if message.content.startswith("!advice"):
            await message.channel.send(random.choice(advice.advice))
            # await message.channel.send((advice.advice)[-1])

        # Help Command
        if message.content.startswith("!help"):
            await message.channel.send(usage.commands)

        # Aaryan Command
        if message.content.startswith("!aaryan"):
            await message.channel.send(biography.bio)

        # Poems Command
        if message.content.startswith("!poem"):
            random_poem = random.choice(list(poems.poems.keys()))
            await message.channel.send(f'''
            Presenting "{random_poem}" by Aaryan Tawde
            \n{poems.poems[random_poem]} 
            ''')

        # Gamer Time Response
        if message.content.startswith("http"):
            game = message.content.split("//")[1]
            game = game.split(".")[0]
            if game in basic_utilities.supported_games:
                await message.channel.send(
                    f"Bruh, you guys still play {game.capitalize()}?")


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
