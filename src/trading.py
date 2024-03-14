import requests

from dotenv import load_dotenv
import os

load_dotenv()
key-id = os.getenv("APCA-API-KEY-ID")
secret-id = os.getenv("APCA-API-SECRET-KEY")

headers2 = {'APCA-API-KEY-ID': key-id,
            'APCA-API-SECRET-KEY': secret-id,
            'accept': 'application/json'}

def get_options_data(headers, date):
    url = "https://paper-api.alpaca.markets/v2/options/contracts?underlying_symbols=AAPL"
    r = requests.get(url, headers=headers2)
    return r.text
    
print(get_options_data(["NVDA"], "2024-03-14"))

# import requests
#
# url = "https://paper-api.alpaca.markets/v2/options/contracts"
#
# headers = {
#     "accept": "application/json",
#     "APCA-API-KEY-ID": "PKRA2LYIZE6YNJWVE5CS",
#     "APCA-API-SECRET-KEY": "aPLl1tmpWzgzrgtysZDH0ftzshyrlv5hMig8y8pz"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.text)
