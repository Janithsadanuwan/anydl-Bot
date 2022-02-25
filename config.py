import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5022185084:AAEK4os3aTLF4m6FXTlK-Ictcnr6fQC3W5k")

    APP_ID = int(os.environ.get("APP_ID", 7997077))

    API_HASH = os.environ.get("API_HASH", "342e484fb4cbb728f7e442f077d22c2d")
