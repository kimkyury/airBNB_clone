from django.core.management.base import BaseCommand
from django_seed import Seed 
from users.models import User

class Command(BaseCommand):

    help = "This command creates many users"
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type = int, help="How many users do you wnat to create"
        )
    
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # all_user = user_models.User.objects.all() # !! 데이터가 클 경우, user.objects.all사용 금지

        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))