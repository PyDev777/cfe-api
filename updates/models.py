import json
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{{user}}/{{filename}}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):

    def serialize(self):
        list_values = list(self.values("user", "content", "image", "id"))
        json_dumps_list_values = json.dumps(list_values)
        return json_dumps_list_values


class UpdateManager(models.Manager):

    def get_queryset(self):
        qs = UpdateQuerySet(self.model, using=self._db)
        return qs


class Update(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        image = self.image.url if self.image and hasattr(self.image, 'url') else ""
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user_id,
            "image": image
        }
        json_dumps_data = json.dumps(data)
        return json_dumps_data
