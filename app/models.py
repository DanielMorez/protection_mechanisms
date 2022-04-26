from django.contrib.auth.models import User
from django.db import models


class Subscribe(models.Model):
    started = models.DateTimeField(
        verbose_name='Started',
        editable=True
    )
    ended = models.DateTimeField(
        verbose_name='Ended',
        editable=True
    )
    user = models.ForeignKey(
        User,
        related_name='subscribes',
        on_delete=models.CASCADE
    )
    social_media = models.URLField(
        null=True,
    )
    address = models.EmailField(
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        null=True,
    )

    class Meta:
        ordering = ('started',)

    def __str__(self):
        return f"{self.user.username}: {self.started} - {self.ended}"
