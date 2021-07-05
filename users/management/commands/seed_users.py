from django.core.management.base import BaseCommand
from django_seed import Seed 
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many users"
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type = int, help="How many users do you wnat to create"
        )
    

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all() # !! 데이터가 클 경우, user.objects.all사용 금지

        seeder.add_entity(room_models.Room, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Amenities created!"))  