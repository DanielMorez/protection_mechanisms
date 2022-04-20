from rest_framework import serializers

from app.models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('started', 'ended', 'user')
