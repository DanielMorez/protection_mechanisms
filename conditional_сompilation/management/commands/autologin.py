from django.core.management.commands.runserver import (
    Command as RunserverCommand,
)
from django.conf import settings


class Command(RunserverCommand):
    help = "Запустить приложение с автоматической авторизацией"
    user = "admin"

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument("-u", action='store', dest='user', type=str)

    def handle(self, *args, **options):
        self.user = options["user"]
        settings.AUTOLOGIN_USER = options["user"]
        super(Command, self).handle(*args, **options)


