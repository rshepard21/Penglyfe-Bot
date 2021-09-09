"""
Adi before starting this bot, please use pip install discord.py, it is the needed package to run this file.
After installed create a new empty tmux session and run this file with python penglyfe.py

:) bot ready.
"""
import discord

intents = discord.Intents.all()

def index_in_list(items, index):
	return index < len(items)

class Penglyfe(discord.Client):

	async def on_ready(self):
		print('Logged in as {0}'.format(self.user))

	async def on_member_update(self, before, after):
		game_before = [i for i in before.activities if str(i.type) == "ActivityType.playing" and str(i.name) == "Penglyfe"]
		game_after = [i for i in after.activities if str(i.type) == "ActivityType.playing" and str(i.name) == "Penglyfe"]

		channel = self.get_channel(885388958450724864)
		if game_before:
			return
		elif game_after:
			await channel.send('{0} is logged on Penglyfe!'.format(before.name))

client = Penglyfe(intents=intents)
client.run('token_goes_here')