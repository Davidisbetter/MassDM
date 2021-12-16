import discord

token = "NjE2NzgyNzkzMTA3ODMyODYy.YbuyIg.Y9tgNO05-RiAzFmJM7xWPGLadzM"
message = "----------------ᴀ ꜱᴇʀᴠᴇʀ-------------------
_[+] ᴄʜᴇᴀᴘ ꜰɪᴠᴇᴍ ɢᴀɴɢ ɪɴᴛʀᴏꜱ.
[+]  ᴄᴏᴏʟ ɢᴏᴏᴅ ɢꜰx
[+]  ᴄʜᴇᴀᴘ ɢᴏᴏᴅ ᴄʟᴏᴛʜɪɴɢ.
[+]  ɢɪᴠᴇᴀᴡᴀʏꜱ-
[+]  ᴄᴜꜱᴛᴏᴍ ᴘꜰᴘꜱ ᴀɴᴅ ʙᴀɴɴᴇʀꜱ
https://discord.gg/ufhfb9QmguE"

client = discord.Client()

@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass

    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass
            
client.run(token, bot=True)
