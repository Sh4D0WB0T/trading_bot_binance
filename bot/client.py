import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )

        self.client.FUTURES_URL = os.getenv("BASE_URL")

    def test_connection(self):
        return self.client.futures_account_balance()

    def place_order(self, **params):
        return self.client.futures_create_order(**params)