from django.db import models
from core import models as core_models

# Create your models here.

class Room (core_models.TimeStampedModel):  #상속받았군

    """Room Model Definition """


    name = models.CharField(max_lenght = 140)
    
    