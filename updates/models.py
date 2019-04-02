print()
print('---> MODELS.PY')


import json
from django.conf import settings
from django.db import models
from django.core.serializers import serialize


def upload_update_image(instance, filename):
    return "updates/{{user}}/{{filename}}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    print('')
    print('--> [QuerySet]')

    # def serialize(self):
    #     qs = self
    #     return serialize("json", qs, fields=('user', 'content', 'image'))

    # def serialize(self):
    #     print('->[QuerySet].serialize()')
    #     # print('[QuerySet].serialize() BEFORE qs = self')
    #     qs = self
    #     # print('[QuerySet].serialize() AFTER qs = self')
    #     final_array = []
    #     for obj in qs:
    #         print('[QuerySet].serialize() BEFORE stuct = json.loads(obj.serialize())')
    #         stuct = json.loads(obj.serialize())
    #         print('[QuerySet].serialize() AFTER stuct = json.loads(obj.serialize())')
    #         final_array.append(stuct)
    #     print('<-[QuerySet].serialize()')
    #     return json.dumps(final_array)

    def serialize(self):
        print()
        print('-> [QuerySet].serialize()')
        # print('[QuerySet].serialize() BEFORE list_values = list(self.values("user", "content", "image", "id"))')
        list_values = list(self.values("user", "content", "image", "id"))
        # print('[QuerySet].serialize() AFTER list_values = list(self.values("user", "content", "image", "id"))')
        print('<- [QuerySet].serialize()')
        return json.dumps(list_values)

    print('<-- [QuerySet]')


class UpdateManager(models.Manager):
    print('')
    print('--> [Manager]')

    def get_queryset(self):
        print()
        print('-> [Manager].get_queryset()')
        # print('[Manager].get_queryset() BEFORE qs = UpdateQuerySet(self.model, using=self._db)')
        qs = UpdateQuerySet(self.model, using=self._db)
        # print('[Manager].get_queryset() AFTER qs = UpdateQuerySet(self.model, using=self._db)')
        print('<- [Manager].get_queryset()')
        return qs

    print('<-- [Manager]')


class Update(models.Model):
    print('')
    print('--> [Model]')

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)

    # print('->[Model] BEFORE objects = UpdateManager()')
    objects = UpdateManager()
    # print('<-[Model] AFTER objects = UpdateManager()')

    def __str__(self):
        print()
        print('[Model].__str__')
        return self.content or ""

    def serialize(self):
        print()
        print('-> [Model].serialize()')
        # return serialize("json", [self], fields=('user', 'content', 'image'))

        # print('[Model].serialize() BEFORE json_data = serialize("json", [self], fields=(...))')
        # json_data = serialize("json", [self], fields=('user', 'content', 'image'))
        # print('[Model].serialize() AFTER json_data = serialize("json", [self], fields=())')
        # return json_data

        # stuct = json.loads(json_data)
        # print(stuct)
        # data = json.dumps(stuct[0]['fields'])
        # print('<- [Model].serialize()')
        # return data

        image = self.image.url if self.image and hasattr(self.image, 'url') else ""
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user_id,
            "image": image
        }
        data = json.dumps(data)
        print('<- [Model].serialize()')
        return data

    print('<-- [Model]')


print('<--- MODELS.PY')
