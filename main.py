import os
import discord
from server import keep_alive
import basic_utilities, advice, poems, biography, usage, facts, memes
import json
from datetime import date
import re
import random

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} is in the house!")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == 'Are you having a great day?' and user != client.user:
        if reaction.emoji == '👎':
            await reaction.message.channel.send(
                f"It's probably because of me, {user.name}")
            await reaction.message.delete()
        else:
            await reaction.message.channel.send(
                f"I don't really care, {user.name}")

            await reaction.message.delete()
@client.event
async def on_message(message):
    if message.author != client.user:

        # Insult Command
        if message.content.startswith("!insult "):
            await message.channel.send(basic_utilities.insult_output(message))

        # Advice Command
        if message.content.startswith("!advice"):
            await message.channel.send(
                (f"```{random.choice(advice.advice)}```"))

        # Help Command
        if message.content.startswith("!help"):
            await message.channel.send(usage.commands)

        # Aaryan Command
        if message.content.startswith("!aaryan"):
            await message.channel.send(biography.bio)

        # Poems Command
        if message.content.startswith("!poem"):
            await message.channel.send(poems.output(message))

        # Fact Command
        if message.content.startswith("!fact"):
            await message.channel.send(facts.output(message))

        # Memes Command
        if message.content.startswith("!meme"):
            await message.channel.send(memes.output())

        # Set Birthday Command
        if message.content.startswith("!setbirthday"):
            date_entered = message.content.split(" ")[1]
            username = message.author.name
            if re.search(r'^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', date_entered):
                file = open("storage/birthdays.json", "r+")
                json_object = json.load(file)
                birthday_list = json_object["birthdays"]
                file.close()

                file = open("storage/birthdays.json", "w")
                for i in range(len(birthday_list)):
                    if list(birthday_list[i].keys())[0] == username:
                        json_object["birthdays"].remove(birthday_list[i])
                        break

                json_object["birthdays"].append({username: date_entered})
                json.dump(json_object, file)
                file.close()
                await message.channel.send(f"```Birthday set as {date_entered} for {username}.```")
            else:
                await message.channel.send(f"```Invalid formatting. Use the mm/dd/yyyy format to input your birthday, {username}.```")

        # Print Birthday Command
        if message.content.startswith("!printbirthday"):
            file = open("storage/birthdays.json", 'r+')
            json_object = json.load(file)["birthdays"]
            username = message.author.name
            for i in range(len(json_object)):
                if list(json_object[i].keys())[0] == username:
                    birthday = json_object[i][username]
                    break
            
            file.close()
            await message.channel.send(birthday)

        # Checkin Command
        if message.content.startswith("!checkin"):
            msg = await message.channel.send("Are you having a great day?")
            reactions = ['👍', '👎']
            for emoji in reactions:
                await msg.add_reaction(emoji)

        # Gamer Time Response
        if message.content.startswith("http"):
            await message.channel.send(basic_utilities.gamer_output(message))


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
