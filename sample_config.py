HEROKU = True  #

# 
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# 
if not HEROKU:
    Bot_token = "7050622921:AAFTho868fxMRS03fyluB6xGrSBUFSPzKco"
    ARQ_API_KEY = "UXGAJY-MIQTOU-KGKSLD-HKQNWW-ARQ"
