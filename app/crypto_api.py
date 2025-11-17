from typing import Any
import requests

from app.constants import BASE_URL, COINMARKETCAP_API_KEY, COINMARKETCAP_SYMBOLS


def get_response() -> requests.Response:
    try:
        response = requests.get(
            url=BASE_URL,
            headers={
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY,
            },
            params={"symbol": COINMARKETCAP_SYMBOLS},
            timeout=10,
        )
        response.raise_for_status()
        return response

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}") from e


def get_json_data() -> dict[str, Any]:
    response = get_response()
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON response: {e}") from e


def transform(data: dict[str, Any]) -> dict[str, Any]:
    try:
        coin_data = next(iter(data["data"].values()))
        crypto_data = next(iter(coin_data))
        quote_dict = crypto_data["quote"]
        base_currency = next(iter(quote_dict))
        quote_data = quote_dict[base_currency]

        return {
            "symbol": crypto_data.get("symbol"),
            "last_updated": quote_data.get("last_updated"),
            "base_currency": base_currency,
            "price": quote_data.get("price"),
            "percent_change_24h": quote_data.get("percent_change_24h"),
        }

    except (StopIteration, KeyError, TypeError, AttributeError) as e:
        raise RuntimeError(f"Invalid API response structure: {e}") from e


def get_crypto_data() -> dict[str, Any]:
    json_data = get_json_data()
    return transform(json_data)
