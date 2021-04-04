from django.contrib import admin
from . import models
# Register your models here.


# 이러면 Amenity가 관리창에선 복수형으로 뜨는데, amenities가 맞음 -> models에 가서 class로 바꿔주자.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """ """
    pass