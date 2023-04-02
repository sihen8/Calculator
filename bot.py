from discord import *
from discord.ext import commands
from calc import *

token = "MTA3NzgwNTgxNTc0ODEwODMzOQ.GLylEX.w2c0TmYMaQ36lpD_gaGwYRrJxOQpIahFJRlahQ"


class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author.id == self.user.id:
            return

        elif message.content.startswith("!calculate"):
            equation = message.content[11:len(message.content)]
            try:
                x = solve_this(equation)
                await message.reply(f"The answer is {x}, did i get it right?")
            except:
                await message.reply("Sorry, i didnt understand the expression")

        elif message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

        elif message.content.startswith("!help"):
            await message.reply("""
            Commands:
            `!help : lists commands`
            `!hello : reply to you with hello`
            `!calculate : do quick maths`
            """)


intents = Intents.default()
intents.message_content = True

client = MyClient(intents=intents, command_prefix="`")
client.run(token)
