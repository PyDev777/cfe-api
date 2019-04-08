import json
import requests

BASE_URL = 'http://192.168.1.5:8000/'
ENDPOINT = 'api/status/'


# def do(method='get', data=None, id=19, is_json=True):
#
#     new_data = {} if data is None else data
#
#     if is_json:
#         new_data = json.dumps(new_data)
#
#     r = requests.request(method, BASE_URL + ENDPOINT + "?id=" + str(id), data=new_data)
#
#     print('status_code = ', r.status_code)
#     print("headers['content-type'] = ", r.headers['content-type'])
#     print()
#     if r.status_code == requests.codes.ok:
#         print('Status code is:', r.status_code, '(OK)')
#         print('r.json():', r.json())
#     else:
#         print('Status code is:', r.status_code, '(NON-200!)')
#         print('r.text = ', r.text)
#     return


def do(method='get', data={}, is_json=True):

    # new_data = {} if data is None else data
    # print()
    print('DO DATA:', data)
    headers = {}

    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    r = requests.request(method, BASE_URL + ENDPOINT, data=data, headers=headers)

    print('status_code = ', r.status_code)
    print("headers['content-type'] = ", r.headers.get('content-type', None))
    # print()
    if r.status_code == requests.codes.ok:
        print('Status code is:', r.status_code, '(OK)')
        print('r.json():', r.json())
    else:
        print('Status code is:', r.status_code, '(NON-200!)')
        print('r.text = ', r.text)
    return


# do(data={'id': 20})
do(method='delete', data={'id': 22})

# do(method='put', data={'id': 20, 'user': 1, 'content': 'PUT!!!'})
# do(method='post', data={'user': 1, 'content': 'POST!!!'})
