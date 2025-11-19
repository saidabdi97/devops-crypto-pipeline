import requests
from .constants import COINS, CURRENCY, API_BASE_URL

def get_crypto_prices():
    url = f"{API_BASE_URL}/simple/price"
    params = {
        "ids": COINS,
        "vs_currencies": CURRENCY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
