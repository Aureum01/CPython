import requests
import json

def get_crypto_price(crypto):
    access_key = '[Enter your API]' # API entered here
    response = requests.get(f"http://api.coinlayer.com/live?access_key={access_key}&expand=1")
    data = json.loads(response.text)
    if data["success"]:
        return data["rates"][crypto.upper()]["rate"]
    else:
        return "API request was not successful. Please check the API key or the cryptocurrency name."

def main():
    crypto = input("Enter the name of the cryptocurrency: ").upper()
    print(f"The current price of {crypto} is: ${get_crypto_price(crypto)}")

main()
