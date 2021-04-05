import discord
import os
import time

client = discord.Client()
token = os.getenv("TOKEN")
min_kakera = 500 # Edit this value

@client.event
async def on_connect():
	print(f'Logged in as: {client.user.name}#{str(client.user.discriminator)}')

@client.event
async def on_message(message):
	if message.author.id == 432610292342587392 and len(message.embeds) != 0:
		embed = message.embeds[0]
		if embed.color.value != 16751916 and embed.color.value != 1360437:
			return #Now we only have to deal with unlaimed $m or $im and the ones wished for

		for line in embed.description.split('\n'):
			if 'roulette' in line:
				return
			if '<:kakera' in line:
				lower = line.index('**') + 2
				upper = lower + line[lower:].index('**')
				kakera = int(line[lower:upper])
				if kakera >= min_kakera or len(message.mentions) != 0:
					time.sleep(0.6) #Mfing mudae has low latency
					await message.add_reaction('❤️')
				return

client.run(token, bot = False)