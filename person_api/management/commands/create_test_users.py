from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create test users'

    def handle(self, *args, **options):
        # Create admin user
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

        # Create guest user
        User.objects.create_user('guest', 'guest@example.com', 'guestpass')

        self.stdout.write(self.style.SUCCESS('Test users created successfully.'))
