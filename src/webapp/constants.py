import os
import dotenv

dotenv.load_dotenv()

API_BASE_URL = "https://api.coingecko.com/api/v3"

COINS = os.getenv("COINS", "bitcoin,ethereum")
CURRENCY = os.getenv("CURRENCY", "usd")

UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
