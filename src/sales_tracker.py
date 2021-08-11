import requests
import json
from time import time

url = "https://api.opensea.io/api/v1/events"


def get_lasthour_sales():
    t_now = time()
    t_query = t_now - 3600

    querystring = {"asset_contract_address":"0x5e34dAcDa29837F2f220D3d1aEAAabD1eDCa5BD1","event_type":"successful","only_opensea":"false","offset":"0","limit":"100","occurred_after":str(t_query)}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)
    response = response['asset_events']
    return len(response)
