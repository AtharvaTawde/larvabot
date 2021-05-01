import os
import discord
from server import keep_alive
import random

client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    supported_games = [
        "shellshock", "krunker", "splix", "slither", "mope", "fortnite"
    ]
    roasts = [
        "Get a life, ", "You don't have aim, ", "Get some skill, ",
        "What's the name of your hack client, ", "Yer bad, ",
        "Even Aaryan's better than you, "
    ]
    advice = [
        "Run out of ice? Use frozen vegetables for your drinks."
        "Are you falling behind your chores? Why not put some clean dishes in the draining rack so it looks like you’re working on it?",
        "Planning to cut down on your food expenses? Wake up late. That way, you’ll miss breakfast and save money.",
        "You can always use your imagination if you can’t afford a virtual reality headset.",
        "No hair? No problem! Draw it or get a tattoo.",
        "Want to beat the morning rush? Combine brushing your teeth with your breakfast.",
        "Leaving your wipers up will stop police officers from giving you a parking ticket.",
        "Use a pepper as a cup so you won’t have to wash it after.",
        "Fill a glove with warm water (and draw a smiley face) the next time you feel lonely.",
        "Use toothpaste if you run out of nail polish.",
        "Plaster can heal all wounds…and even repair your car.",
        "Tired of boiling water every night? Heat 10 liters of water, place them on empty soda plastic bottles and freeze for future use.",
        "Having a bad day? Wear sunglasses. Now you’re having a bad evening.",
        "Don’t have flashlight on your phone? Take a photo of the sun and use that to find your way in the dark.",
        "Aaryan is the best.", "CHICKEN IS YUM."
    ]

    poems = {
        "Moon and Sun":
        "Oh, those days when the sun and moon were alike\nBut now the moon envies the sun for it is so bright\nThe sun envies the cool dark night",
        "Lava":
        "I was in lava\nMy body was roasting fast\nIn the orange lake",
        "Ain":
        "I am Ain\nI am pain\nI like plane\nI have no brain\nI am a big stain\nI have no brain\nI like plane\nI am pain\nI am Ain",
        "Ze Soviets are coming!!":
        "Storm ze Reichstag\nPut Soviet phlag\nDrink some Molotov too!",
        "Lavender":
        "The purple flower\nSmells of just like morning dew\nOnly to wilt soon"
    }

    if message.author != client.user:

        # Insult Command
        if message.content.startswith("!insult"):
            target = message.content.split(" ")[1]
            await message.channel.send(random.choice(roasts) + target)

        # Advice Command
        if message.content.startswith("!advice"):
            await message.channel.send(random.choice(advice))

        if message.content.startswith("!help"):
            await message.channel.send("""
            Commands for L∆rv∆ Bot:
            !insult [name]: Insults the targeted person
            !advice: Gives you a random piece of useful advice
            """)

        # Aaryan Command
        if message.content.startswith("!aaryan"):
            await message.channel.send("""
            Aaryan, aka Aaryabhata, is a very great gamer and human. Aaryan has a godly gamer skill, in which he turn into a rainbow colored baby goat. Aaryan s so great, he can do a flip. He likes to swin in chocolate, and eat ice cream. Palak paneer and "roti paratha with garam masala" are among his favorite dishes, as well as a "chicken samosa" at times. Type '!poem for more info' about the great Aaryan. 
            '''

        # Poems Command
        if message.content.startswith("!poem"):
            random_poem = random.choice(list(poems.keys()))
            await message.channel.send(
            f'''
            Presenting "{random_poem}" by Aaryan Tawde
            {poems[random_poem]} 
            ''')

        # Gamer Time Command
        if message.content.startswith("http"):
            game = message.content.split("//")[1]
            game = game.split(".")[0]
            if game in supported_games:
                await message.channel.send(
                    f"Bruh, you guys still play {game.capitalize()}?")


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
