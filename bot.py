


import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle
import logging
import logging.config

 

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

 


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from info import LOG_CHANNEL, ON_HEROKU, CLONE_MODE, PORT
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from server import web_server

 

import asyncio
from pyrogram import idle
from plugins.clone import restart_bots
from bot import TheBlackBot
from utils.keepalive import ping_server
from bot.clients import initialize_clients

 


ppath = "plugins/*.py"
files = glob.glob(ppath)
TheBlackBot.start()
loop = asyncio.get_event_loop()

 


async def start():
    print('\n')
    print('Initalizing Tech VJ Bot')
    bot_info = await TheBlackBot.get_me()
    TheBlackBot.username = bot_info.username
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Tech VJ Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    me = await TheBlackBot.get_me()
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    app = web.AppRunner(await web_server())
    await TheBlackBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    if CLONE_MODE == True:
        await restart_bots()
    print("Bot Started Powered By @VJ_Botz")
    await idle()

 

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')


 
