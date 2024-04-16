import pprint
import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image
from obj_size import get_size

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass


json_response = response.json()

map_api_server = "http://static-maps.yandex.ru/1.x/"
point = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["Point"]["pos"]
longitude, lattitude = point.split(" ")
ll = longitude + '' + lattitude
point = f'{longitude},{lattitude},pm2grm'
map_scale = get_size(json_response)
map_scale['pt'] = point
response = requests.get(map_api_server, params=map_scale)
Image.open(BytesIO(
    response.content)).show()
