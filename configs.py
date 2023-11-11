# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "18051748"))
    API_HASH = getenv("API_HASH", "941f76b6cb94ad88d27abe96a25c3ba6")
    BOT_TOKEN = getenv("BOT_TOKEN", "6323337513:AAHOmEGnYfBAadhq1h1eVH8CrTRI9Tfrl2g")
    FSUB = getenv("FSUB", "WMchannelS")
    CHID = int(getenv("CHID", "-1001953506128"))
    SUDO = list(map(int, getenv("SUDO", "1918917066").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://SERIAL:SERIAL@cluster0.m6omsjh.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
