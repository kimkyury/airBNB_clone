from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models


# AbstrafctItem은 Roomtypes에서 필요하다
# Amenity Types(편의시설 유형), facilities(시설) House Rules(사용규칙) 관련된 것들도 관련있다
# 
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    # Meta 클래스란 모든 class 내부에 있는 class래.
    class meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition """
    # RoomType object를를 admin panel에 추가/삭제하고 싶어서.

    class Meta:
        # verbose_name_plural안해주면 장고가 이름 + s 를 기본값으로 해버린다.
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):
    """ Amenity model definition """
    
    class Meta:
        # verbose_name_plural안해주면 장고가 이름 + s 를 기본값으로 해버린다.
        verbose_name_plural = "Amenities"



class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        # verbose_name_plural안해주면 장고가 이름 + s 를 기본값으로 해버린다.
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        # verbose_name 안 해주면 장고가 Camel기법을 쓰지 않고 그냥 해버린다
        verbose_name_plural = "House Rule"

    
class Photo(core_models.TimeStampedModel):
    """Photo Model Definition """

    # 사진은 각 캡션을 가진다 (간단설명)
    caption = models.CharField(max_length=200)
    file = models.ImageField()

    # room은 Photo와 연결되어야함.
    # room을 지우면 photo도 지워야하니 forignkey에 room집어넣음
    # 파이썬은 파일을 상하수직방향으로 읽어서, class Room보다 이 함수가 더 밑에 위치해야함
    # 그래서, foretignKey(room, ~)을 ForetignKey("Room", ~) 처럼 그 값을 문자열 취급해주면 된다.
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    # clas를 위해 STring방법을 정의해야한다
    def __str__(self):
        return self.caption
    

class Room (core_models.TimeStampedModel):  # 상속받았군

    """ Room Model Definition """
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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # 한사람에게 여러 객실 유형을 선택하지 못하도록 할거임
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)     # 다대다관계
    amenities = models.ManyToManyField("Amenity",  blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule",  blank=True)


def __str__(self):
    return self.name
