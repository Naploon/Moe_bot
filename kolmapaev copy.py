import discord
from discord.ext import commands
import youtube_dl
import os


TOKEN = "NzkxNjU4NDUwNjU5ODM1OTE0.X-SXYg.RlvRg9RcIgTGBjOHHwQruiZ62b8"

#pmst see osa on bot
client = commands.Bot(command_prefix="!")

#kommandid
@client.event
async def on_ready():
    
    gens_uma_sumus = client.get_channel(108263953250951168)

    await gens_uma_sumus.send("tra ma faking poon üles ennast")


@client.event
async def on_message(message):

    if message.content == "kolmapäev":
        tymmisucc = client.get_channel(205421648214622214)
        await tymmisucc.send("WOOooOO WEDNESDAY WOOOooOOooOOOOO LET'S GOOOOOOO")



#siit alla proovin selle asja muusikat saada mängima

@client.command()
async def moe_play(ctx, url : str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("hey hEY HEY. You cant just start playing one song on top of an another one. If you cant for the current song to finish get outta my bar or use the 'stop' command")
        return




    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='magnar')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    


    ydl_opts = {'format' : 'bestaudio/best', 'postprocessors' : [{'key' : 'FFmpegExtractAudio', 'preferredcodec' : 'mp3', 'preferredquality' : '192', }], }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("song.mp3"))



@client.command()
async def moe_leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Guys, u havent invited me to any channels so ive got nowhere to go. Heh reminds me of christmas when i had nowhere to go")

@client.command()
async def moe_pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("I wasnt event playing anything. Why would you just shut me up?")

@client.command()
async def moe_resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("minig bläma siia sisse veel")

@client.command()
async def moe_stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


#jooksuta clientit serveris

client.run(TOKEN)
