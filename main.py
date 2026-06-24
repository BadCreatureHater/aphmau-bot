import discord
from discord.ext import commands
import asyncio
import datetime
import random
import os
import sys
client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True  # Required to read message text

@client.event
async def on_ready():
    print(f'Sucecessfully logged in')

    await bot.change_presence(
    activity=discord.Activity(type=discord.ActivityType.watching, name="my trash bin") 
    )

    bot = commands.Bot(command_prefix="++", intents=intents)

    @bot.command()
    async def info(ctx):
         embed = discord.Embed(
        title="Aphmau bot info and stats",
        description="Something about me",
        color=discord.Color.blue()
    )
         embed.add_field(name="STATS", value="NO STATS TO SHOW.", inline=False)
         embed.add_field(name="MAIN FULL COMMANDS", value="++say: make my say something" \
         "++askaph: ask me anything", inline=False)
         embed.add_field(name="STAFF ONLY COMMANDS", value="++kick: kick em out" \
         "++ban: ban em out", inline=False)
         embed.add_field(name="MADE WITH", value="discord.py", inline=False)
         embed.add_field(name="ORIGINAL BOT", value="https://discord.com/oauth2/authorize?client_id=1519121589621231717", inline=False)
         embed.add_field(name="GITHUB REPO", value="https://github.com/BadCreatureHater/aphmau-bot", inline=False)
    
         
         
         
         await ctx.send(embed=embed)
         
         @bot.command
         async def askaph(ctx, *, question):
              responses = [
                   "Yes, I'm the queen of trash!",
                   "No.",
                   "YES! UWU",
                   "NO!",
                   "What are ABCs?",
                   "Help me! i don't know what is 9 + 10 Equals!",
                   "Note: My Brain is made with carbon dioxide and idiotness",
                   "What are Integers? They are positive and negative numbers?"
                   "*turns into a trash bin*",
                   "*eats toilet*",
                   "*makes clickbait videos*",
                   "*watches baby shows*",
                   "*becomes a logokid and starts watching watching logo effects*"
              ]
              answer = random.choice(responses)
              await ctx.send("Your Question: {question}" \
              "My Answer: {answer}")

              async def askapherror(ctx, error):
               if isinstance(error, commands.MissingRequiredArgument):
                       embed = discord.Embed(
        title="SOMETHING IS WRONG!",
        description="HUH?",
        color=0xe74c3c
    )
                       
                       embed.set_footer(
    text="You didn't ask me something, please use ``++askaph do you like lemonade``"
)
                       await ctx.send(embed=embed)
    @bot.command()
    async def say(ctx, *, content: str):
          await ctx.message.delete()
          await ctx.send(content)

    @bot.command()
    async def kick(ctx, member: discord.Member, *, reason: str = "No reason provided"):
     await member.kick(reason=reason)
     await ctx.send(f"Successfully kicked **{member.name}** for: *{reason}*")
     if member.top_role >= ctx.guild.me.top_role:
        await ctx.send("I cannot kick this user because their role is higher than or equal to mine.")
        return
       
    @bot.command()
    async def ban(ctx, member: discord.Member, *, reason: str = "No reason provided"):
         await member.ban(reason=reason, delete_message_days=1)
         await ctx.send(f"Successfully banned {member.mention} for: {reason}")
         if member.top_role >= ctx.guild.me.top_role:
             await ctx.send("I cannot ban this user.")

             bot.run("YOURTOKENHERE")
