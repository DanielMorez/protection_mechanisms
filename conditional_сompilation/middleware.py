from django.contrib import auth
from django.contrib.auth.middleware import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import settings


class AutomaticUserLoginMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        if settings.AUTOLOGIN_USER and not AutomaticUserLoginMiddleware._is_user_authenticated(request):
            user = User.objects.filter(username=settings.AUTOLOGIN_USER).first()
            if user:
                request.user = user
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    @staticmethod
    def _is_user_authenticated(request):
        user = request.user
        return user and user.is_authenticated