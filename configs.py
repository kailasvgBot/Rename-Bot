# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "21967179"))
    API_HASH = os.environ.get("API_HASH", "37d5fbb9217cb56d6261e61305d92748")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6157657126:AAHozWAymWNAl8yjtHj0eI5GvymjewgSH1U")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "5963778687"))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://darshana:darshana@cluster0.elq2jqs.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001942355657"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
