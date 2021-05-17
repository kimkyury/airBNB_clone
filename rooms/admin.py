from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.room)
class RommAdmin(admin.ModelAdmin):

    pass