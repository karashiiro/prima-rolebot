import discord
import os

class Prima(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_socket_raw_receive(self, message):
		string = message[1]
		print(string)

client = Prima()
client.run(os.environ['DISCORD_BOT_TOKEN'])
