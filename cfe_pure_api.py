import json
import requests

BASE_URL = 'http://192.168.1.6:8000/'
ENDPOINT = 'api/updates/'


def get_list():
    print()
    print('--> get_list()')
    r = requests.get(BASE_URL + ENDPOINT)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()

    data = r.json()
    print('data:', data)
    print('type(data) is', type(data))
    print('type(json.dumps(data)) is', type(json.dumps(data)))
    print()

    for obj in data:
        print()
        print('obj[id]:', obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print('r2:', r2)
            print('type(r2) is', type(r2))
            print('r2.json():', r2.json())
            print('type(r2.json()) is', type(r2.json()))
            print()
            print('dir(r2) is', dir(r2))

    # print('data:', data)
    print()
    print('<-- get_list()')
    return data


def create_update():
    print()
    print('--> create_update()')

    new_data = {
        'user': 1,
        'content': 'Hello, this is content from user 1!'
    }

    r = requests.post(BASE_URL + ENDPOINT, data=new_data)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()

    if r.status_code == requests.codes.ok:
        print('r.json():', r.json())
        print()
        print('<-- create_update()')
        return r.json()
    else:
        print('ERROR! ')
        print('text = ', r.text)
        print()
        print('<-- create_update()')
        return r.text


def delete_list():
    print()
    print('--> delete_list()')

    new_data = {
        'user': 1,
        'content': 'Hello, this is content from user 1!'
    }

    # r = requests.delete(BASE_URL + ENDPOINT, data=new_data)
    r = requests.delete(BASE_URL + ENDPOINT)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()

    if r.status_code == requests.codes.ok:
        print('r.json():', r.json())
        print()
        print('<-- delete_list()')
        return r.json()
    else:
        print('ERROR! ')
        print('text = ', r.text)
        print()
        print('<-- delete_list()')
        return r.text


# get_list()
create_update()
# delete_list()
