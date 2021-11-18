
from telethon import events 
import time 
import asyncio 
from userbot.events import register

@register(outgoing=True,pattern="^.[Ss]iri")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Siri Yazmak Yerine__ `.sancaklar` __Yazmalısın.__\n \n**Gerekli Açıklama:** t.me/SancaklarUsersBot/65 \n UserBot Kanalı: @SancaklarUsersBot\nPlugin Kanalı: @sancaklarPlugin")

@register(outgoing=True,pattern="^.[Ee]pic")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Epic Yazmak Yerine__ `.sancaklar` __Yazmalısın.__\n \n**Gerekli Açıklama:** https://t.me/SancaklarUsersBot/80 \n UserBot Kanalı: @SancaklarUsersBot\nPlugin Kanalı: @sancaklarPlugin")
