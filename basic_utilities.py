import random
supported_games = [
    "shellshock", "krunker", "splix", "slither", "mope", "fortnite"
]

roasts = [
    "Get a life, ", "You don't have aim, ", "Get some skill, ",
    "Bro, yer doodoo! Turn off yer hack client, ", "Yer bad, ",
    "Even Aaryan's better than you, "
]


def gamer_output(message):
    game = message.content.split("//")[1]
    game = game.split(".")[0]
    if game in supported_games:
        return f"```Bruh, you guys still play {game.capitalize()}?```"
    else:
        return ''

def insult_output(message):
    if message.content != "!insult":
        split_command = message.content.split(" ")
        new_command = split_command
        del new_command[0]
        target = " ".join(new_command)
        if "larva" in target.lower() or "bot" in target.lower():
            return f"```I do not allow that. {random.choice(roasts)} {message.author}```"
        else:
            return f"```{random.choice(roasts) + target}```"
    else:
        return "```Usage: !insult [name of person you wanna roast]```"