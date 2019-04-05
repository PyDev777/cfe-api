import json
import requests

BASE_URL = 'http://192.168.1.5:8000/'
ENDPOINT = 'api/updates/'


def get_list(id=None):

    new_data = {} if id is None else {'id': id}

    r = requests.get(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()
    if r.status_code == requests.codes.ok:
        print('Status code is:', r.status_code, '(OK)')
        print('r.json():', r.json())
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('r.text = ', r.text)
    return


def create_update():
    new_data = {
        'user': 1,
        'content': 'Update 4 from create_update()',
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()
    if r.status_code == requests.codes.ok:
        print('Status code is:', r.status_code, '(OK)')
        print('r.json():', r.json())
        return r.json()
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('r.text = ', r.text)
        return r.text


def delete_list():
    r = requests.delete(BASE_URL + ENDPOINT)
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()
    if r.status_code == requests.codes.ok:
        print('r.json():', r.json())
        return r.json()
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('r.text = ', r.text)
        return r.text


def do_obj_update():
    new_data = {
        'id': 3,
        'content': 'obj Update 1 by method PUT',
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is:', r.status_code, '(OK)')
        print('r.json():', r.json())

    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('r.text = ', r.text)
    return


def do_obj_delete():
    new_data = {
        'id': 21,
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is:', r.status_code, '(OK)')
        print('r.json():', r.json())
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('text = ', r.text)
    return


get_list()
# create_update()
# delete_list()
# do_obj_update()
# do_obj_delete()
