import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
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
        all_users = user_models.User.objects.all() # !! 데이터가 클 경우, user.objects.all사용 금지

        room_types = room_models.RoomType.objects.all()
        print(room_types, all_users)


        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host' : lambda x: random.choice(all_users),
            'room_type' : lambda x :random.choice(room_types),
            'guests': lambda x:random.randint(0,20),
            'price': lambda x:random.randint(0,300),
            'beds': lambda x:random.randint(0,5),
            'bedrooms': lambda x:random.randint(0,5),
            'baths': lambda x:random.randint(0,5),

        },)
        created_photos = seeder.execute()
        self.stdout.write(self.style.SUCCESS("Amenities created!"))  