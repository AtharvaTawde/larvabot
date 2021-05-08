import random, re, json

supported_games = [
    "shellshock", "krunker", "splix", "slither", "mope", "fortnite", "skribbl"
]

game_complaints = ["Not "]

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
        return ""


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


def birthday_output(message):
    date_entered = message.content.split(" ")[1]
    username = message.author.name
    if re.search(r'^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', date_entered):
        file = open("storage/birthdays.json", "r+")
        json_object = json.load(file)
        print(json_object, "Step 1 Complete!")
        json_object[username] = date_entered
        print("Updated data: Step 2 Complete!")
        json.dump(json_object, file)
        print("Sent data: Step 3 Complete!")
        file.close()
        return f"```Birthday set as {date_entered} for {username}.```"
    else:
        return f"```Invalid formatting. Use the mm/dd/yyyy format to input your birthday, {username}.```"
