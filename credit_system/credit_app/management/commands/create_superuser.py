from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    help = 'Создание суперпользователя, если он не существует.'

    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан.'))
        else:
            self.stdout.write(self.style.SUCCESS('Суперпользователь уже существует.'))