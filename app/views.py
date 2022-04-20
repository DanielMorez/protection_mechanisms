from rest_framework import generics

from app.models import Subscribe
from app.serializers import SubscribeSerializer


class SubscribeAPIView(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

