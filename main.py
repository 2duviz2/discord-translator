import discord #Imports the discord module.
from discord.ext import commands #Imports discord extensions.
from deep_translator import GoogleTranslator


intents = discord.Intents.default()
intents.message_content = True
intents.guild_reactions = False
intents.members = False

messagesAlreadyTranslated = []


client = commands.Bot(command_prefix= ">", intents=intents)

client.remove_command("help")

@client.event
async def on_ready():
    print("Bot ready")
    await client.change_presence(activity=discord.Game(">tranₑₙ >tradₑₛ"))

@client.command()
async def tran(ctx):
    if(ctx.channel.fetch_message):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        if message not in messagesAlreadyTranslated:
            messagesAlreadyTranslated.append(message)
            translated = GoogleTranslator(source='auto', target='en').translate(message.content)
            await ctx.send(translated)

@client.command()
async def trad(ctx):
    if(ctx.channel.fetch_message):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        if message not in messagesAlreadyTranslated:
            messagesAlreadyTranslated.append(message)
            translated = GoogleTranslator(source='auto', target='es').translate(message.content)
            await ctx.send(translated)

client.run("BOT TOKEN!")
