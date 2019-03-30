import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/updates/'


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)

    # print('status_code = ', r.status_code)
    # print("headers['content-type'] = ", r.headers['content-type'])
    # print('encoding = ', r.encoding)
    # print('text = ', r.text)

    data = r.json()
    # print('data = ', data)
    # print('type(data) is ', type(data))
    # print('type(json.dumps(data)) is ', type(json.dumps(data)))
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
            # print('type is', type(r2.json()))
            # print('dir is', dir(r2))

    return data


get_list()
