from django.contrib import admin
from . import models  #같은 폴더에 있는 models를 데려온다
# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass