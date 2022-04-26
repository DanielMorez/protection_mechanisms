from django.urls import path

from app.views import SubscribeAPIView, SubscribeRetrieve, SubscribeSQL

urlpatterns = [
    path('subscribes', SubscribeAPIView.as_view()),
    path('subscribes/<int:user_id>', SubscribeRetrieve.as_view()),
    path('subscribes-sql', SubscribeSQL.as_view())
]
