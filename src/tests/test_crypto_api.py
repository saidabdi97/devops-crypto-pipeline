import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.insert(0, PROJECT_ROOT)

from webapp.crypto_api import get_crypto_prices


def test_get_crypto_prices_basic():
    data = get_crypto_prices()
    assert isinstance(data, dict)
    assert "bitcoin" in data
    assert "ethereum" in data
    assert "usd" in data["bitcoin"]
