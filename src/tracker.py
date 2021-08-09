import requests
import json


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def get_token_info():
    url = "https://api.opensea.io/api/v1/assets"

    querystring = {"token_ids": "8713", "asset_contract_address": "0xf621b26ce64ed28f42231bcb578a8089f7958372",
                   "order_direction": "desc", "offset": "0", "limit": "20"}

    response = requests.request("GET", url, params=querystring)

    response = json.loads(response.text)
    response = response['assets'][0]
    output = dict()
    desired_keys_list = ['name','id','image_url','description']
    for key, value in response.items():
        if key in desired_keys_list:
            output[key] = value
    return output
