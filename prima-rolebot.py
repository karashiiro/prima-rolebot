import configparser
import discord
import os
import pymongo

class Prima(discord.Client):
	def __init__(self):
		self.config = configparser.RawConfigParser();
		self.config.read("config");
		self.db = pymongo.MongoClient("mongodb://localhost:27017/")[self.config.get("database_name")];

	async def on_ready(self):
		print("Logged on as {0}!".format(self.user))

	async def on_socket_raw_receive(self, message):
		string = message[1]
		print(string)

client = Prima()
client.run(os.environ["DISCORD_BOT_TOKEN"])
