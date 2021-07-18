from django import forms
from . import models

class SearchForm(forms.Form):
    
    city = forms.CharField(initial="Anywhere")
    price = forms.IntegerField(required = False)
    room_type = forms.ModelChoiceField(queryset = models.RoomType.objects.all())  #모델초이스는 쿼리셋이 필요함

