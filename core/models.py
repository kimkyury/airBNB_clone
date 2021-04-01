from django.db import models


# 이 클래스는 로그인, 가입기록이 있는 User를 빼고 이용시키도록 할 것임
# Create your models here.
class TimeStampedModel (models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True