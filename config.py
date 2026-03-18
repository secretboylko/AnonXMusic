from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # 🔐 Correct getenv usage
        self.API_ID = int(getenv("API_ID", "31656328"))
        self.API_HASH = getenv("API_HASH", "a9e57623a4408a41418ca647b2f08950")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8596610814:AAHWlaVig5-Il-Wb7-mOu7NUtxVyhk280is")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://aditya0:aditya0@cluster0.9m8897t.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003858465326"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8335505032"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        # 🎵 Sessions
        self.SESSION1 = getenv("SESSION", "BACcYO4AInYlvyCFpKzoEfEm8FjsDjUEgZR-Cn50cCiXyUNNcvgEienoH_sknXmwLDTBiB_s390XB7QTt5YtQcV_Uu7D5VR4UvEwswKxTocJvPVtiArxG5kIJW5U3HY4kYBrilw5n65easW2hXlA9EEGdcArlAHxjVqb33FXtQ-sab_updP-95lTIQrBlEQQCM1qPLacXxBD2KTeWQvu7wpet4t961-z8J5qbYK_3yk1cOaLJoaip2syh3Lld_-JXSMbyA8Xq-WBsJEf0TKEsVm1-xVyrdjRfk9K37-2WbCf2bW4TS1WIruXwGm8ZRf-Id6EsRAuVZylTLThbGg3K1VjNSNBcQAAAAF1LT2ZAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        # 📢 Support
        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Neet_Study_Matarial")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/song_assistant")

        # ⚙️ Flags
        self.AUTO_LEAVE = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END = getenv("AUTO_END", "False").lower() == "true"
        self.THUMB_GEN = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        # 🍪 Cookies (FIXED – any URL works)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://pastebin.com/raw/6HfsrYMp").split(" ")
            if url
        ]

        # 🖼️ Images
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var for var in [
                "API_ID",
                "API_HASH",
                "BOT_TOKEN",
                "MONGO_URL",
                "LOGGER_ID",
                "OWNER_ID",
                "SESSION1"
            ] if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
