from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials'

    def add_arguments(self, parser):
        parser.add_argument('--username', default='admin', help='Username for the superuser')
        parser.add_argument('--password', default='admin123', help='Password for the superuser')

    def handle(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User with username {username} already exists')
            )
            return
            
        try:
            user = User.objects.create_superuser(
                username=username,
                password=password,
                role='Admin',
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser with username: {username}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            ) 