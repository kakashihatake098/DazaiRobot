import requests
from telethon import events
from DazaiRobot import telethn as meow

@meow.on(events.NewMessage(pattern="^/cosplay"))
async def waifu(event):
  r = requests.get("https://waifu-api.vercel.app").json() #api credit- @YASH_SHARMA_1807 on telegram
  await event.reply(file=r)
  
@meow.on(events.NewMessage(pattern="^/lewd"))
async def waifu(event):
  r = requests.get("https://waifu-api.vercel.app/items/1").json()
  await event.reply(file=r)

__mod_name__ = "ᴄᴏsᴘʟᴀʏ"
__help__ = """
Just a weeb type module to get anime cosplay and lewd pictures
- /cosplay
- /lewd
"""
