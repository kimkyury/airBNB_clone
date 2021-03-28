from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    """ User Model """   # 이건 docstring임. 파이썬에쓰는 표준형식
                         # 클래스생성시에 넣어서 뭔지 말해주는 거임.
                         # 이걸 가지고 간 admin에서 이름에 마우스 갖다대면
                         # 이 설명문이 뜬 단 말씀



    avatar = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True) # 최대 글자 수 지정
    bio = models.TextField(default="")


