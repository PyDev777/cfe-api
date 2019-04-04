import json
import requests

BASE_URL = 'http://192.168.1.5:8000/'
ENDPOINT = 'api/updates/'


def get_list():
    print()
    print('--> get_list()')
    print()

    r = requests.get(BASE_URL + ENDPOINT)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()
    print('type(requests.get) is', type(r))

    data = r.json()

    print('data:', data)
    print('type(data) is', type(data))
    # print('type(json.dumps(data)) is', type(json.dumps(data)))
    # print()
    # print('type(json.loads(data)) is', type(json.loads(data)))
    print()

    for obj in data:

        print('================')
        print(obj)
        print('================')
        # print()
        # print('obj[id]:', obj['id'])

        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))

            # print('r2:', r2)
            # print('type(r2) is', type(r2))
            print('-----------------------')
            print('status_code = ', r.status_code)
            print("headers['content-type'] = ", r.headers['content-type'])
            print('request.get.id=1.json():', r2.json())
            print('type(request.get.id=1.json()) is', type(r2.json()))
            print('-----------------------')
            # print()
            # print('dir(r2) is', dir(r2))

    # print('data:', data)
    print()
    print('<-- get_list()')
    print()
    return data


def create_new_content():
    print()
    print('--> create_new_content()')
    print()

    new_data = {
        'user': 1,
        'content': 'New content 4',
        'image': '',
    }
    print('new_data:', new_data)
    json_dumps_new_data = json.dumps(new_data)
    print('json_dumps_new_data: ', json_dumps_new_data)

    r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is: OK')
        print('r.json():', r.json())
        print()
        print('<-- create_new_content()')
        return r.json()
    else:
        print('Status code is non-200!)')
        print('text = ', r.text)
        print()
        print('<-- create_new_content()')
        return r.text


def update_existing_content():
    print()
    print('--> update_existing_content()')
    print()

    new_data = {
        'user': 1,
        'content': 'Updated by new content!',
        'image': ''
    }
    print('new_data:', new_data)
    json_dumps_new_data = json.dumps(new_data)
    print('json_dumps_new_data: ', json_dumps_new_data)

    r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data)
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is: OK')
        print('r.json():', r.json())
        print()
        print('<-- update_existing_content()')
        return r.json()
    else:
        print('Status code is non-200!)')
        print('text = ', r.text)
        print()
        print('<-- update_existing_content()')
        return r.text


def create_update():
    print()
    print('--> create_update()')
    print()

    new_data = {
        'user': 1,
        'content': 'Update NEW3',
        'image': ''
    }

    json_dumps_new_data = json.dumps(new_data)

    print('json_dumps_new_data: ', json_dumps_new_data)

    r = requests.post(BASE_URL + ENDPOINT + "1/", data=json_dumps_new_data)

    # print('r.json():', r.json())
    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()

    if r.status_code == requests.codes.ok:
        # print('r.json():', r.json())
        print('Status code is:', r.status_code, '(OK)')
        print()
        print('<-- create_update()')
        return r.json()
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('text = ', r.text)
        print()
        print('<-- create_update()')
        return r.text


def delete_list():
    print()
    print('--> delete_list()')
    print()

    # new_data = {
    #     'user': 1,
    #     'content': 'Hello, this is content from user 1!'
    # }

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


def do_obj_update():
    print()
    print('--> do_obj_update()')
    print()

    new_data = {
        # 'user': 1,
        'content': 'Update by method: PUT)',
        # 'id': 1
    }

    print('new_data:', new_data)
    # json_dumps_new_data = json.dumps(new_data)
    # print('json_dumps_new_data: ', json_dumps_new_data)

    r = requests.put(BASE_URL + ENDPOINT + "1/", data=new_data)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    # print('encoding = ', r.encoding)
    # print('text = ', r.text)
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is: OK')
        print('r.json():', r.json())
        print()
        print('<-- do_obj_update()')
    else:
        print('Status code is non-200!)')
        print('text = ', r.text)
        print()
        print('<-- do_obj_update()')

    return


def do_obj_delete():
    print()
    print('--> do_obj_delete()')
    print()

    r = requests.delete(BASE_URL + ENDPOINT + "1/")

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers['content-type'])
    print()

    if r.status_code == requests.codes.ok:
        print('Status code is: OK')
        print('r.json():', r.json())
        print()
        print('<-- do_obj_delete()')
    else:
        print('Status code is non-200!)')
        print('text = ', r.text)
        print()
        print('<-- do_obj_delete()')

    return


get_list()
create_new_content()
update_existing_content()
create_update()
delete_list()
do_obj_update()
do_obj_delete()

