import json


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except Exception as e:
        print('ERROR!', e)
        is_valid = False
    return is_valid
