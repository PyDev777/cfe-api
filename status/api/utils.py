import json


def is_json(json_data):
    print()
    print('is_json(json_data):', json_data)
    print()
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except Exception as e:
        print('ERROR!', e)
        print()
        is_valid = False
    return is_valid
