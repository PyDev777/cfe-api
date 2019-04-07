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
obj_serializer = StatusSerializer(obj)
obj_json_data = JSONRenderer().render(obj_serializer.data)

obj_stream = io.BytesIO(obj_json_data)
obj_data = JSONParser().parse(obj_stream)


# ------------------------------------------
# Serialize a queryset
# ------------------------------------------

qs = Status.objects.all()
qs_serializer = StatusSerializer(qs, many=True)
qs_json_data = JSONRenderer().render(qs_serializer.data)

qs_stream = io.BytesIO(qs_json_data)
qs_data = JSONParser().parse(qs_stream)




# ------------------------------------------
# Create object
# ------------------------------------------

data = {'user': 1, 'content': 'Comment is Created!'}
create_obj_serializer = StatusSerializer(data=data)

create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()

# if serializer.is_valid():
#     serializer.save()


# ------------------------------------------
# Update object
# ------------------------------------------

obj = Status.objects.first()
data = {'user': 1, 'content': 'Comment is Updated!'}
update_serializer = StatusSerializer(obj, data=data)

update_serializer.is_valid()
update_serializer.save()

# update_serializer.errors


# ------------------------------------------
# Delete object
# ------------------------------------------

data = {'user': 1, 'content': 'Delete me'}
create_obj_serializer = StatusSerializer(data=data)

create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
print(get_data_serializer.data)
print(obj.delete())
