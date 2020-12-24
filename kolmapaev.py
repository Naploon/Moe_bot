import discord

TOKEN = "NzkxNjU4NDUwNjU5ODM1OTE0.X-SXYg.RlvRg9RcIgTGBjOHHwQruiZ62b8"

#pmst see osa on bot
client = discord.Client()


@client.event
async def on_ready():
    #siia alla stuff
    gens_uma_sumus = client.get_channel(108263953250951168)

    await gens_uma_sumus.send("say something gangsta...")


@client.event
async def on_message(message):

    if message.content == "kolmapäev":
        tymmisucc = client.get_channel(205421648214622214)
        await tymmisucc.send("WOOooOO WEDNESDAY WOOOooOOooOOOOO LET'S GOOOOOOO")


#jooksuta clientit serveris

client.run(TOKEN)
