from app.crypto_api import transform, get_response


def test_transform():
    test_fake_data = {
        "data": {
            "BTC": [
                {
                    "id": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "quote": {
                        "USD": {
                            "price": 103929.32609335119,
                            "percent_change_24h": 2.5
                        }
                    }
                }
            ]
        }
    }
    
    result = transform(test_fake_data)

    assert result["symbol"] == "BTC"
    assert result["price"] == 103929.32609335119


def test_response():
    response = get_response()
    assert response.status_code == 200
