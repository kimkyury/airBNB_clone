from django.db import models


# 이 클래스는 로그인, 가입기록이 있는 User를 빼고 이용시키도록 할 것임
# Create your models here.
class TimeStampedModel (models.Model):
    """ Time Stamped Model """


    # DateTime에는 좋은 기능이 있다. which is, auto_now, auto_now_add가 있음. 
    # auto_now를 true하면 save시점의 date와 time을 기록함
    # auto_now_add를 true하면 model생성할 때마다 수시로 업데이트 될 것임 (모델이 생성된 날짜를 구하기)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True