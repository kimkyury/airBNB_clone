from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # 같은 폴더에 있는 models를 데려온다
# Register your models here.

@admin.register(models.User)    # admin.site.register(models.User, CustomUserAdmin) 랑 같은 거다. admin패널에서 이 user를 보고싶단 말~
class CustomUserAdmin(UserAdmin):
    """ Custeom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        ( 
            "Custom Profile", 
            { 
                "fields": (   #파란 타이틀에 올라가는 소제목
                    'avatar', #하위 항목들
                    'gender', 
                    'bio', 
                    'birthdate', 
                    'language', 
                    'currency', 
                    'superhost' 
                )
            }
        ),
    )
