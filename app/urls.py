from django.urls import path

from app.views import SubscribeAPIView

urlpatterns = [
    path('subscribes', SubscribeAPIView.as_view()),
]