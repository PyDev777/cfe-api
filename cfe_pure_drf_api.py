import json
import requests
import os

AUTH_ENDPOINT = 'http://192.168.1.5:8000/api/auth/jwt/'
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'

image_path = os.path.join('drf-logo.jpg')

data = {
    'username': 'dev',
    'password': '1212qwqw'
}

headers = {'content-type': 'application/json'}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
print('status_code = ', r.status_code)
print("headers['content-type'] = ", r.headers.get('content-type', None))
if r.status_code == requests.codes.ok:
    print('Status code is:', r.status_code, '(OK)')
    # print('r.json():', r.json())
    token = r.json().get('token', None)
    print('TOKEN:', token)

    refresh_data = {'token': token}
    r2 = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
    print('status_code (refresh) = ', r2.status_code)
    print("headers['content-type'] (refresh) = ", r2.headers.get('content-type', None))
    if r2.status_code == requests.codes.ok:
        print('Status code is (refresh):', r2.status_code, '(OK)')
        # print('r.json():', r.json())
        token2 = r2.json().get('token', None)
        print('TOKEN (refresh):', token2)
    else:
        print('Status code is (refresh):', r2.status_code, '(NON-200!)')
        print('r2.text (refresh) = ', r2.text)
else:
    print('Status code is:', r.status_code, '(NON-200!)')
    print('r.text = ', r.text)






# -------------------------------------------------------------------------------------------

# BASE_URL = 'http://192.168.1.5:8000/'
# ENDPOINT = 'api/status/'

# get_endpoint = BASE_URL + ENDPOINT + str(25)
# post_data = json.dumps({'content': 'Some random content'})
#
# r = requests.get(get_endpoint)
# print('r.text:', r.text)
#
# r2 = requests.get(BASE_URL + ENDPOINT)
# print('r2.status_code:', r2.status_code)
#
# post_headers = {'content-type': 'application/json'}
#
# post_response = requests.post(BASE_URL + ENDPOINT, data=post_data, headers=post_headers)
#
# print('post_response.text:', post_response.text)


# def do_img(method='get', data={}, is_json=True, img_path=None):
#
#     # new_data = {} if data is None else data
#     # print()
#     print('DO DATA:', data)
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     if image_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {'image': image}
#             r = requests.request(method, BASE_URL + ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, BASE_URL + ENDPOINT, data=data, headers=headers)
#
#     print('status_code = ', r.status_code)
#     print("headers['content-type'] = ", r.headers.get('content-type', None))
#     # print()
#     if r.status_code == requests.codes.ok:
#         print('Status code is:', r.status_code, '(OK)')
#         print('r.json():', r.json())
#     else:
#         print('Status code is:', r.status_code, '(NON-200!)')
#         print('r.text = ', r.text)
#     return


# do_img(method='post', data={'user': 1, 'content': ''}, is_json=False, img_path=image_path)
# do_img(method='put', data={'user': 1, 'id':28, 'content': 'PUT on 28'}, is_json=False, img_path=image_path)


# def do(method='get', data={}, is_json=True):
#
#     # new_data = {} if data is None else data
#     # print()
#     print('DO DATA:', data)
#     headers = {}
#
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     r = requests.request(method, BASE_URL + ENDPOINT, data=data, headers=headers)
#
#     print('status_code = ', r.status_code)
#     print("headers['content-type'] = ", r.headers.get('content-type', None))
#     # print()
#     if r.status_code == requests.codes.ok:
#         print('Status code is:', r.status_code, '(OK)')
#         print('r.json():', r.json())
#     else:
#         print('Status code is:', r.status_code, '(NON-200!)')
#         print('r.text = ', r.text)
#     return


# do(data={'id': 20})
# do(method='delete', data={'id': 22})

# do(method='put', data={'id': 20, 'user': 1, 'content': 'PUT!!!'})
# do(method='post', data={'user': 1, 'content': 'POST!!!'})


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
