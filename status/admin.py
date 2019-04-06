from django.contrib import admin
from .models import Status
from .forms import StatusForm


class StatusAdmin(admin.ModelAdmin):
    form = StatusForm
    list_display = ['id', 'user', '__str__', 'image']


admin.site.register(Status, StatusAdmin)
