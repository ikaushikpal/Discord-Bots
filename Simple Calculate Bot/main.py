import discord
import os
import keep_me_alive
from my_logger import my_logger


client = discord.Client()
logger = my_logger()

@client.event
async def on_ready():
    logger.debug(f"logged as {client.user} and bot is online")


def calculate(s):
    tempRes = list(s.split(' '))
    if len(tempRes) != 3:
        return "Could not understood"

    method, num1, num2 = tempRes
    res = 0

    if method.lower() == 'add':
        res = float(num1) + float(num2)

    elif method.lower() == 'sub':
        res = float(num1) - float(num2)

    elif method.lower() == 'div':
        if num2 == '0':
            return f"Can not divide, because divisor is 0"
        else:
            res = float(num1) / float(num2)

    elif method.lower() == 'mul':
        res = float(num1) * float(num2)

    elif method.lower() == 'mod':
        res = int(num1) % int(num2)
        return str(res)

    else:
        return "Could not understood"

    x = f"{res:0.2f}"
    return f"Result = {str(x)}"


def print_help():
    message = f"{'-'*78}\nWelcome to help section of this bot.\n\nThere are 5 different methods available, i.e.\n\n1.For addition use 'add' command\n2.For subtraction use 'sub' command\n3.For multiplication use 'mul' command\n4.For division use 'div' command\n5.For modulo use 'mod' command\n\nFor example if you write $add 1 1 then BOT will display Result = 2.00\n{'-'*78}"
    return message


@client.event
async def on_message(message):
    if message.author == client.user: # for bot says
        logger.info(f"Bot wrote {message.content}")
        return

    if message.content.startswith("$"):
        logger.debug(f"{message.author} said {message.content}")
        if 'help' in message.content:
            await message.channel.send(print_help())
            return

        result = calculate(message.content[1:])
        await message.channel.send(result)


if __name__ == "__main__":
    logger.debug("PROGRAM STARTED")
    keep_me_alive.alive()
    client.run(os.getenv('TOKEN'))