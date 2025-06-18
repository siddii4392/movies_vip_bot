import re
from os import environ, getenv
from Script import script

# Regex pattern to validate numeric IDs
id_pattern = re.compile(r'^.\d+$')

# Helper function to enable/disable features
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Telegram Bot credentials
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23171419'))
API_HASH = environ.get('API_HASH', 'dc9e22bd05e0dd3d7f8bea3940012509')
BOT_TOKEN = environ.get('BOT_TOKEN', '7952333946:AAHV8bCPK4iQjB44z8wHtgqId-ut4EAMjWs')

# Admins & Channels
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1520536793').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Siddiziya")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002871329356'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+vsGDn1KYlCsxZDY1')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002810547720').split()]

# MongoDB
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sidddiqsarathi:siddiq123@siddiq.2cyvkba.mongodb.net/?retryWrites=true&w=majority&appName=Siddiq")
DATABASE_NAME = environ.get('DATABASE_NAME', "siddiq")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Logging & Support
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '0'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', '0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '0')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')  # Must be admin

# Verification System
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'), True)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# Shortener settings
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", SHORTENER_API)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", SHORTENER_WEBSITE)
SHORTENER_API3 = environ.get("SHORTENER_API3", SHORTENER_API)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", SHORTENER_WEBSITE)

# Content filters
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024, 2002, -1)]
SEASONS = [f'season {i}' for i in range(1, 23)]

# Referral System
REF_PREMIUM = 30
PREMIUM_POINT = 1500

# Auth Channel check
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# Images
START_IMG = environ.get('START_IMG', 'https://i.ibb.co/qpxpGmC/image.jpg').split(',')
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = environ.get("REFER_PICS", "https://envs.sh/PSI.jpg").split()
PAYPICS = environ.get('PAYPICS', 'https://envs.sh/_kA.jpg').split()
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg')
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]

# Bot Behavior Settings
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled(environ.get('AUTO_FILTER', 'True'), True)
IS_PM_SEARCH = is_enabled(environ.get('IS_PM_SEARCH', 'False'), False)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', 'True'), True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled(environ.get('IMDB', 'False'), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get('LONG_IMDB_DESCRIPTION', 'False'), False)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', 'False'), False)
SPELL_CHECK = is_enabled(environ.get('SPELL_CHECK', 'True'), True)
LINK_MODE = is_enabled(environ.get('LINK_MODE', 'True'), True)
MAX_BTN = int(environ.get('MAX_BTN', '8'))

# Stream Mode
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', 'True'), True)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # in seconds

# Heroku Check
ON_HEROKU = 'DYNO' in environ
URL = environ.get("FQDN", "")

# Final Settings Dictionary
SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}'),
    'caption': environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}'),
    'tutorial': TUTORIAL,
    'shortner': SHORTENER_WEBSITE,
    'api': SHORTENER_API,
    'shortner_two': SHORTENER_WEBSITE2,
    'api_two': SHORTENER_API2,
    'log': LOG_VR_CHANNEL,
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY,
    'verify_time': TWO_VERIFY_GAP,
    'shortner_three': SHORTENER_WEBSITE3,
    'api_three': SHORTENER_API3,
    'third_verify_time': THREE_VERIFY_GAP
}
