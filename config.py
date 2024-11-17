import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27429920
API_HASH = "10225d977fb7fa0d97ea30d2378bcd22"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7301314460:AAGmmUrdsm0OPOUV1y2j4NdeRGPd_xM6iic"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Zoro:Heyzoro@cluster0.o9sr4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002175738368

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6882001052

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/thanos_pro"
SUPPORT_GROUP = "https://t.me/thanosprosss"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGijCAABBZk0eNIVkfACpWLVeuDtNn1D40VWn4ctAET3Zh5MDpWddLqY9hkSywm2_s6-Q2BSv9Nb0bxM46u7V8ifQVTe2QSCV1waeQ27cmHfpvSitn_D7EJSrad2YJIkAfqtfMvXDM3d6Im5pv4lDaIc6KcJE8giWah5dq5Yve5B4aqfGCnr3JkkHPcjn51kW_pcWQltWk8NkG2825ziFkHmmQOc_Fbhc7g-641WJGnVKRNBFQ79lqKO1eYUJ-j7cuaip6NVwd4O0S_CROsYOxNMtDpBfMMbYgOkx-dEY-Yr7pp1HV5arJyAc5rQERX7rGHI8a9QVgc4RovI5MIiJTCiJfFKAAAAAGhm3HyAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"

PING_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"

PLAYLIST_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
STATS_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
STREAM_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/6040fJ6/photo-2024-11-17-06-48-34-7438137071744581648.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("https://t.me/Angelmusic_support", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("https://t.me/Animefriendsgroup", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
