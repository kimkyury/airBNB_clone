from django.db import models
from core import models as core_models
from django.utils import timezone

class Reservation (core_models.TimeStampedModel):
    
    """ Reservation Model Definition """
    
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices = STATUS_CHOICES, default=STATUS_PENDING
    )

    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
        
    def in_progress(self): # check in/out 날짜가 현재보다 작고 큰지 구분(진행중인지 확인)
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
    
    in_progress.boolean = True  #bool값을 요약이모티콘(X표라든지) 으로 표시

    def is_finished(self): #완료되었는지 체크해보자
        now = timezone.now().date()
        return now > self.check_out
        
    is_finished.boolean = True

