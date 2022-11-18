from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25678011
    API_HASH = "29094b2a38bcad5cd118ddb500cba217"
    # the name to display in your alive message
    ALIVE_NAME = "P4rzivaL"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:rvmUIJq4su33mmXluYj1@containers-us-west-129.railway.app:7714/railway"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = ""
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5741914122:AAER-QZNEbu2HRArim0HEPuQWpkLFkM9XDA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001895888673
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "~"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
