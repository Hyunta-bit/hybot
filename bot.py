import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="주인 병신 ㅋㅋㅋㅋㅋㅋㅋㅋ"))

  print("봇 이름:현타봇",client.user.name,"봇 아이디:810695063981785098",client.user.id,"봇 버전:",discord.__version__)


client.run(os.environ['token'])