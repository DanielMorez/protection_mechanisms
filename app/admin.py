from django.contrib import admin

from app import models


@admin.register(models.Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'started', 'ended')
    list_editable = ('user', 'started', 'ended')

