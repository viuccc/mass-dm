import discord
from discord.ext import commands
import asyncio
import time
prefix = "_"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')



@bot.event
async def on_ready():
    print(bot.user.name)
    print('Online')
    print('started.......')
    print('Created with 💖 daman saini#0605🤗')
 #   while True:
    #	await bot.change_presence(status=discord.Status.invisible)

# while True: 	
 #  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers''')) 	
   

@bot.command(name="ping")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
		
@bot.command(name="dm")
@commands.has_role('daman')
async def f(ctx,*,msg):
	await ctx.message.delete()
	author=ctx.message.author
	
	for guild in bot.guilds:
		for member in guild.members:
			try:
				await member.send(msg)
				embed=discord.Embed(title='''Sending Everyone DM''',description=f'''DM sent to {member.name}#{member.discriminator}''' ''' ✅ ''',colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				embed.set_footer(text="</> with 💖daman saini#0605🤗",icon_url="https://cdn.discordapp.com/attachments/716917641209708647/732917420347490314/722399728507027466.png")
				await ctx.send(embed=embed)
			except:
				embed=discord.Embed(title='''Sending Everyone DM''',description=f'''DM not sent to {member.name}#{member.discriminator}''' ''' ❌ ''',colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				embed.set_footer(text="</> with 💖daman saini#0605🤗",icon_url="https://cdn.discordapp.com/attachments/716917641209708647/732917420347490314/722399728507027466.png")
				await ctx.send(embed=embed)
					
				embed=discord.Embed(title="DM sent to all",description=f" :white_check_mark: ",colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_footer(text="</> with 💖daman saini#0605🤗",icon_url="https://cdn.discordapp.com/attachments/671588139713822750/685906211786588282/JPEG_20200214_212403.jpg")
				await ctx.send(embed=embed)
@f.error
async def f_error(ctx,error):
    if isinstance(error,commands.CheckFailure):
    	embed=discord.Embed(title="Discord DM",description="**LoL you not have enough permission daman to use this command** :joy: ",colour=0x142c9c)
    	embed.set_image(url="https://cdn.discordapp.com/attachments/539066238870224903/606135147913543693/Tw_1-1-1.gif")
    	embed.set_footer(text="</> with 💖 daman saini#0605🤗")
    	await ctx.send(embed=embed)
    if isinstance(error,commands.MissingRequiredArgument):
    	await ctx.send(f"Please say a message to send!")

		
bot.run("NzUxMTE3MTc4ODU3NTg2ODQ5.X1EaYg.x8lYGFJVHvYuO5zBNEMULOlCyu8")  # Where 'TOKEN' is 
