from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{{user}}/{{filename}}".format(user=instance.user, filename=filename)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)

    def __str__(self):
        return self.content or ""
