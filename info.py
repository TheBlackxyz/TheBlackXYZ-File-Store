import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
PICS = (environ.get('PICS', 'https://graph.org/file/517bc12dd5c1347df10f6.jpg')).split()
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :- DATABASE 
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False
CLONE_DATABASE_URI = environ.get("CLONE_DATABASE_URI", "")
CLONE_DATABASE_NAME = environ.get("CLONE_DATABASE_NAME", "")

# DATABASE INFORMATION....
DATABASE_URI = environ.get("DATABASE_URI", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True))
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) 
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) 

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True Then Fill All or False
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "t.me/TheBlackXYZ")

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', True)) # Set True or False
WEBSITE_URL = environ.get("WEBSITE_URL", "")

# File Streaming 
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")


 
    
