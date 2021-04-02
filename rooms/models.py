from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

class Room (core_models.TimeStampedModel):  # 상속받았군

    """Room Model Definition """
    name = models.CharField(max_length=140)
    description = models.TextField()
    contry = CountryField()
    city = models.CharField(max_length=80)

    price = models.IntegerField()
    address = models.CharField(max_length=140)

    guests = models.IntegerField()

    # 침대, 침실, ...
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()   # 0-24
    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)  # room이랑 user랑 연결되어야 한다