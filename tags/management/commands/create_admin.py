from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = "Create a superuser with default credentials"

    def handle(self, *args, **kwargs):
        username = "admin"
        email = "admin@example.com"
        password = os.getenv("ADMIN_PASSWORD", "admin")  # Uses env variable if set, otherwise "admin"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
