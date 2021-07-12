from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from math import ceil
# Create your views here.

def all_rooms(request):
    page = request.GET.get("page",1)
    room_list = models.Room.objects.all() #쿼리셋 생성
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(int(page))

    return render(request, "rooms/home.html",  {"rooms": rooms})
    

