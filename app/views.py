from rest_framework import generics, response

from django.db import connection

from app.models import Subscribe
from app.serializers import SubscribeSerializer


class SubscribeAPIView(generics.ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    filterset_fields = ('user_id',)


class SubscribeRetrieve(generics.RetrieveAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class SubscribeSQL(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET['user_id']
        sql = f"SELECT * FROM app_subscribe WHERE user_id LIKE {query};"
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql)
            except Exception as e:
                cursor.executescript(sql)
            row = cursor.fetchall()
        return response.Response(row)
