# from fx import account as ac
# from fx import oanda_common as oc
import account as ac
import common as oc
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20 import API
import json


api = API(access_token=ac.access_token, environment=oc.OANDA_ENV.PRACTICE)

params = {"instruments": "USD_JPY"}
ps = PricingStream(ac.account_ID, params)

try:
    for rsp in api.request(ps):
        print("■リストの取得")
        print(json.dumps(rsp, indent=2))

        print("■bidsのみ抽出：")
        if "bids" in rsp.keys():
            print(rsp["bids"][0]["price"])


except V20Error as e:
    print("Error: {}".format(e))

'''
https: // takilog.com/oandaapi-get-pricingstream/
'''
