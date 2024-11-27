HEROKU = True  #

# 
if HEROKU:
    from os import environ

    Bot_token = environ["7050622921:AAFTho868fxMRS03fyluB6xGrSBUFSPzKco"]
    ARQ_API_KEY = environ["UXGAJY-MIQTOU-KGKSLD-HKQNWW-ARQ"]

# 
if not HEROKU:
    Bot_token = "7050622921:AAFTho868fxMRS03fyluB6xGrSBUFSPzKco"
    ARQ_API_KEY = "UXGAJY-MIQTOU-KGKSLD-HKQNWW-ARQ"
