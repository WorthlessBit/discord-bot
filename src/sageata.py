import discord
import sys
import os

client = discord.Client()
token = os.environ['token']

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

	if "logout()" == message.contet.lower():
		await client.close()
		sys.exit()

client.run(token)