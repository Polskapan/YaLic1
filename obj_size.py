params = {}


def get_size(jason):
    toponym = jason["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    envelope = toponym['boundedBy']['Envelope']
    lower, upper = envelope['lowerCorner'].split(' '), envelope['upperCorner'].split(' ')
    d1 = str(float(upper[0]) - float(lower[0]))
    d2 = str(float(upper[1]) - float(lower[1]))
    params = \
        {
            'll': ','.join([toponym_longitude, toponym_lattitude]),
            'spn': ','.join([d1, d2]),
            'l': 'map'
        }
    return params
