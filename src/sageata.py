import discord
import sys


client = discord.Client()
token = open("config.txt", "r").read()

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message)
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

	if "logout()" == message.contet.lower():
		await client.close()
		sys.exit()

client.run(token)