# https://www.django-rest-framework.org/api-guide/serializers/

# ------------------------------------------
import json

data = {'abc': 123}
data_list = ['abc']

data_json = json.dumps(data)
print(data_json)

load_json = json.loads(data_json)
print(load_json)

print(load_json['abc'])


# ------------------------------------------
from status.models import Status
from status.api.serializers import StatusSerializer

obj = Status.objects.first()
print(obj)

data = StatusSerializer(obj)
print(data)
print(data.data)
# print(json.loads(data.data))

from rest_framework.renderers import JSONRenderer

new_json_data = JSONRenderer().render(data.data)

print(new_json_data)

print(json.loads(new_json_data))


# ------------------------------------------
# Works only on interactive console: from django.utils.six import BytesIO
# Better use in apps code: from io import BytesIO
import io
from rest_framework.parsers import JSONParser

json1 = new_json_data

stream = io.BytesIO(json1)
data = JSONParser().parse(stream)
print(data)

# ------------------------------------------
qs = Status.objects.all()
serializer = StatusSerializer(qs, many=True)
print(serializer.data)

json_data = JSONRenderer().render(serializer.data)
print(json_data)
print(json.loads(json_data))
stream = io.BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)
