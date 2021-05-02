import os
import discord
from server import keep_alive
import basic_utilities, advice, poems, biography, usage, facts, memes

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} is in the house!")


@client.event
async def on_message(message):
    if message.author != client.user:

        # Insult Command
        if message.content.startswith("!insult "):
            await message.channel.send(basic_utilities.insult_output(message))

        # Advice Command
        if message.content.startswith("!advice"):
            await message.channel.send(advice.output)

        # Help Command
        if message.content.startswith("!help"):
            await message.channel.send(usage.commands)

        # Aaryan Command
        if message.content.startswith("!aaryan"):
            await message.channel.send(biography.bio)

        # Poems Command
        if message.content.startswith("!poem"):
            await message.channel.send(poems.output)

        # Fact Command
        if message.content.startswith("!fact"):
            await message.channel.send(facts.output(message))
        
        # Memes Command
        if message.content.startswith("!meme"):
            await message.channel.send(memes.output())

        # Gamer Time Response
        if message.content.startswith("http"):
            await message.channel.send(basic_utilities.gamer_output(message))


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
