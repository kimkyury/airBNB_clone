from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Custom User Model """   # docstring, 이 클래스가 쓰일때 마우스에 갖다대면 이 설명문이 표시됨
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
        )
    
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "en"), (LANGUAGE_KOREAN, "ko")
        )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True) # 최대 글자 수 지정
    bio = models.TextField(default="", blank=True)
    
    birthdate = models.DateField(null=True)
    langaue = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    
    superhost = models.BooleanField(default=False)