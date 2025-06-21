from os import getenv
from dotenv import load_dotenv
load_dotenv()
TOKEN = getenv('BOT_TOKEN')
PG_USER = getenv('PG_USER')
PG_PASS = getenv('PG_PASS')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')
PG_DB = getenv('PG_DB')
if __name__ == '__main__':
    print(PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB)