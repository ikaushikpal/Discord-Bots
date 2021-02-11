import discord
import os
import alive
from my_logger import my_logger
import requests
from dotenv import load_dotenv
# pip install python-dotenv


load_dotenv()
client = discord.Client()
logger = my_logger()
jokeId = -1


@client.event
async def on_ready():
    logger.debug(f"logged as {client.user} and bot is online")


def getJoke(category):
    global jokeId
    req = requests.get(f"https://v2.jokeapi.dev/joke/{category}")
    json = req.json()
    if json['error'] == True:
        if 'message' in json:
            return json['message']
        else:
            return "Unable to fetch joke"

    msg = '' 
    if jokeId == json['id']:
        return getJoke(category)
    jokeId = json['id']    
    if json['type'] == 'single':
        msg = json['joke']
    else:
        msg = json['setup'] + '\n'
        msg += json['delivery']
    return msg


def filterJoke(msg):
    splitedMsg = list(msg.split(' '))
    if len(splitedMsg) > 2:
        return "Invalid Command"
    if len(splitedMsg) == 1:
        return 'any'
    
    else:
        category = splitedMsg[1]
        return category

def print_help():
    message = f"{'='*78}\nWelcome to help section of this JOKE bot.\n\nThere are 6 different category available, i.e.\nany, misc, programming, dark, pun, spooky and christmas\n\nFor example if you write \n!joke dark then BOT will display any dark joke available on internet\n{'='*78}"
    return message


@client.event
async def on_message(message):
    if message.author == client.user: # for bot says
        logger.info(f"Bot wrote {message.content}")
        return

    if message.content == '!joke help':
        await message.channel.send(print_help())
        return

    if message.content.startswith("!joke"):
        category = filterJoke(message.content[1:])
        msg = getJoke(category)
        print(msg)
        return await message.channel.send(msg)
        
@client.event
async def on_member_join(member):
    print("hello 1")
    msg = f'Welcome {member.name} 😎, Hope you will like it 😃'
    await member.create_dm()
    return await member.dm_channel.send(msg)

@client.event
async def on_member_remove(member):
    print("hello 2")
    msg = f'Goodbye {member.name} 😢'
    await member.create_dm()
    return await member.dm_channel.send(msg)


if __name__ == "__main__":
    logger.debug("PROGRAM STARTED")
    # alive.alive()
    client.run(os.getenv('TOKEN'))