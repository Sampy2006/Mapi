from main_window import *

import requests
from PIL import Image

import sys
from io import BytesIO
import json


def paint(address_ll, delta, l='sat', point=False):
    org_point = "{0},{1}".format(address_ll[0], address_ll[1])

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join(address_ll),
        "spn": ",".join([delta, delta]),
        "l": l
    }

    if point:
        map_params['pt'] = "{0},pm2dgl".format(org_point)

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    return response
