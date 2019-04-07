# https://www.django-rest-framework.org/api-guide/serializers/


# --> python manage.py shell

import json
from status.models import Status
from status.api.serializers import StatusSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


# ------------------------------------------
# Serialize a single object
# ------------------------------------------

obj = Status.objects.first()
# print(obj)

obj_serializer = StatusSerializer(obj)
# print(obj_serializer)
# print(obj_serializer.data)

obj_json_data = JSONRenderer().render(obj_serializer.data)
# print(obj_json_data)
# print(json.loads(obj_json_data))

obj_stream = io.BytesIO(obj_json_data)
# print(obj_stream)

obj_data = JSONParser().parse(obj_stream)
# print(obj_data)


# ------------------------------------------
# Serialize a queryset
# ------------------------------------------

qs = Status.objects.all()
# print(qs)

qs_serializer = StatusSerializer(qs, many=True)
# print(qs_serializer)
# print(qs_serializer.data)

qs_json_data = JSONRenderer().render(qs_serializer.data)
# print(qs_json_data)
# print(json.loads(qs_json_data))

qs_stream = io.BytesIO(qs_json_data)
# print(qs_stream)

qs_data = JSONParser().parse(qs_stream)
# print(qs_data)


'''
/home/dev/Proj/restapi2/bin/python3.6 /home/dev/Downloads/pycharm-2018.3.4/helpers/pydev/pydevconsole.py --mode=client --port=44073

import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend(['/home/dev/Proj/restapi2/src/cfeapi', '/home/dev/Downloads/pycharm-2018.3.4/helpers/pycharm', '/home/dev/Downloads/pycharm-2018.3.4/helpers/pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run("/home/dev/Proj/restapi2/src/cfeapi")
PyDev console: starting.

Python 3.6.8 (default, Dec 24 2018, 19:24:27) 
[GCC 5.4.0 20160609] on linux
Django 1.11.20

>>> import json
... from status.models import Status
... from status.api.serializers import StatusSerializer
... from rest_framework.renderers import JSONRenderer
... import io
... from rest_framework.parsers import JSONParser

>>> obj = Status.objects.first()
>>> obj
<Status: Status Content 1...>

>>> obj_serializer = StatusSerializer(obj)
>>> obj_serializer
StatusSerializer(<Status: Status Content 1...>):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    content = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
    image = ImageField(allow_null=True, max_length=100, required=False)
>>> obj_serializer.data
{'user': 1, 'content': 'Status Content 1', 'image': None}

>>> obj_json_data = JSONRenderer().render(obj_serializer.data)
>>> obj_json_data
b'{"user":1,"content":"Status Content 1","image":null}'
>>> json.loads(obj_json_data)
{'user': 1, 'content': 'Status Content 1', 'image': None}

>>> obj_stream = io.BytesIO(obj_json_data)
>>> obj_stream
<_io.BytesIO object at 0x7f9fe9236830>

>>> obj_data = JSONParser().parse(obj_stream)
>>> obj_data
{'user': 1, 'content': 'Status Content 1', 'image': None}

>>> 

>>> qs = Status.objects.all()
>>> qs
<StatusQuerySet [<Status: Status Content 1...>, <Status: 13...>]>

>>> qs_serializer = StatusSerializer(qs, many=True)
>>> qs_serializer
StatusSerializer(<StatusQuerySet [<Status: Status Content 1...>, <Status: 13...>]>, many=True):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    content = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
    image = ImageField(allow_null=True, max_length=100, required=False)
>>> qs_serializer.data
[OrderedDict([('user', 1), ('content', 'Status Content 1'), ('image', None)]), OrderedDict([('user', 1), ('content', '13'), ('image', None)])]

>>> qs_json_data = JSONRenderer().render(qs_serializer.data)
>>> qs_json_data
b'[{"user":1,"content":"Status Content 1","image":null},{"user":1,"content":"13","image":null}]'
>>> json.loads(qs_json_data)
[{'user': 1, 'content': 'Status Content 1', 'image': None}, {'user': 1, 'content': '13', 'image': None}]

>>> qs_stream = io.BytesIO(qs_json_data)
>>> qs_stream
<_io.BytesIO object at 0x7f9fe92368e0>

>>> qs_data = JSONParser().parse(qs_stream)
>>> qs_data
[{'user': 1, 'content': 'Status Content 1', 'image': None}, {'user': 1, 'content': '13', 'image': None}]

'''