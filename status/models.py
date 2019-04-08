from django.conf import settings
from django.db import models


def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):

    pass


class StatusManager(models.Manager):

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_status_image, blank=True, null=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:45] + '...'

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
