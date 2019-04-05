import json


def is_json(json_data):
    print()
    print('-> is_json(json_data)')
    print()
    print('Incoming data:', json_data)
    print('Incoming data TYPE:', type(json_data))
    try:
        print('Try...')
        real_json = json.loads(json_data)
        print('real_json:', real_json)
        is_valid = True
    except Exception as e:
        print('ERROR!', e)

        is_valid = False

    print('is_valid:', is_valid)

    print('<- is_json(json_data)')
    print()
    return is_valid
