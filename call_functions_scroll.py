import os
import requests

SCROLL_KEY = os.environ["SCROLL_KEY"]
CONTRACT = "0xC65754d990c4098b9147cAD31acAe440f8b0202e"


class ScrollCalls:

    def __init__(self):
        self.url_erc20 = (f"https://api-sepolia.scrollscan.com/api?module=account&action=tokentx&contractaddress="
                          f"{CONTRACT}&page=1&offset=100&sort=asc&apikey={SCROLL_KEY}")

    def call_token(self):

        response = requests.get(self.url_erc20)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"La solicitud GET falló con el código de estado: {response.status_code}")
            data = {"error": "error conection"}

        return dict(data)
