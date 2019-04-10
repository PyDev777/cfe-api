import json
import requests
import os


AUTH_ENDPOINT = 'http://192.168.1.5:8000/api/auth/register/'

image_path = os.path.join('drf-logo.jpg')

data = {
    # 'username': 'dev',
    # 'username': 'pydev@ukr.net',
    'username': 'sysadmin12',
    'email': 'pydev2@ukr.net',
    'password': '1212qwqw',
    'password2': '1212qwqw'
}

headers = {
    'content-type': 'application/json',
    # 'Authorization': 'JWT ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRldiIsImV4cCI6MTU1NDgyNTY3NiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU1NDgyNTM3Nn0.Xlqh5Ssw3v_cQ7HUNtxehe9ahbTQ7VWiL6msFT781d0',
}
# token = None

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)

print()
print('status_code = ', r.status_code)
print("headers['content-type'] = ", r.headers.get('content-type', None))

print('r.json():', r.json())

# token = r.json().get('token', None)
# print('TOKEN:', token)
#
# detail = r.json().get('detail', None)
# print('Detail:', detail)
print()


# ---------------------------------------------------------------------------------------------

# AUTH_ENDPOINT = 'http://192.168.1.5:8000/api/auth/'
#
# image_path = os.path.join('drf-logo.jpg')
#
# data = {
#     # 'username': 'dev',
#     'username': 'pydev@ukr.net',
#     'password': '1212qwqw'
# }
#
# headers = {
#     'content-type': 'application/json',
#     # 'Authorization': 'JWT ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRldiIsImV4cCI6MTU1NDgyNTY3NiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU1NDgyNTM3Nn0.Xlqh5Ssw3v_cQ7HUNtxehe9ahbTQ7VWiL6msFT781d0',
# }
# # token = None
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
#
# print()
# print('status_code = ', r.status_code)
# print("headers['content-type'] = ", r.headers.get('content-type', None))
#
# print('r.json():', r.json())
#
# # token = r.json().get('token', None)
# # print('TOKEN:', token)
# #
# # detail = r.json().get('detail', None)
# # print('Detail:', detail)
# print()


# ---------------------------------------------------------------------------------------------

# AUTH_ENDPOINT = 'http://192.168.1.5:8000/api/auth/jwt/'
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
#
# ENDPOINT = 'http://192.168.1.5:8000/api/status/'
#
# image_path = os.path.join('drf-logo.jpg')
#
# data = {
#     'username': 'dev',
#     'password': '1212qwqw'
# }
#
# headers = {'content-type': 'application/json'}
# token = None
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# print('status_code = ', r.status_code)
# print("headers['content-type'] = ", r.headers.get('content-type', None))
# if r.status_code == requests.codes.ok:
#     print('Status code is:', r.status_code, '(OK)')
#     # print('r.json():', r.json())
#     token = r.json().get('token', None)
#     print('TOKEN:', token)
#
#     # refresh_data = {'token': token}
#     # r2 = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
#     # print('status_code (refresh) = ', r2.status_code)
#     # print("headers['content-type'] (refresh) = ", r2.headers.get('content-type', None))
#     # if r2.status_code == requests.codes.ok:
#     #     print('Status code is (refresh):', r2.status_code, '(OK)')
#     #     # print('r.json():', r.json())
#     #     token2 = r2.json().get('token', None)
#     #     print('TOKEN (refresh):', token2)
#     # else:
#     #     print('Status code is (refresh):', r2.status_code, '(NON-200!)')
#     #     print('r2.text (refresh) = ', r2.text)
#
#     if token:
#
#         # post_data = {'content': 'Some random 3 content and JWT'}
#         post_data = {'content': 'PUT2 content and JWT'}
#
#         jwt_headers = {
#             # 'content-type': 'application/json',
#             'Authorization': 'JWT ' + token
#         }
#
#         if image_path is not None:
#             with open(image_path, 'rb') as image:
#                 file_data = {'image': image}
#                 print('file_data (jwt):', file_data)
#                 # r3 = requests.post(ENDPOINT, data=post_data, files=file_data, headers=jwt_headers)
#                 r3 = requests.put(ENDPOINT + str(39) + '/', data=post_data, files=file_data, headers=jwt_headers)
#                 print('status_code (jwt) = ', r3.status_code)
#                 print("headers['content-type'] (jwt) = ", r3.headers.get('content-type', None))
#                 print()
#                 print('r3.text (jwt) = ', r3.text)
#         else:
#             # r3 = requests.post(ENDPOINT, data=post_data, headers=headers)
#             r3 = requests.put(ENDPOINT + str(39) + '/', data=post_data, headers=jwt_headers)
#             print('status_code (jwt) = ', r3.status_code)
#             print("headers['content-type'] (jwt) = ", r3.headers.get('content-type', None))
#             print()
#             print('r3.text (jwt) = ', r3.text)
#
#     else:
#         print()
#         print('TOKEN is None!')
#         print()
# else:
#     print('Status code is:', r.status_code, '(NON-200!)')
#     print('r.text = ', r.text)
