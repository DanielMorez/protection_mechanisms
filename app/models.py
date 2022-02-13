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

    class Meta:
        ordering = ('started',)

    def __str__(self):
        return f"{self.user.username}: {self.started} - {self.ended}"
