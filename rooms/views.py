from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries

from . import models


class HomeView(ListView): # Lendering 할 필요가 없어졌음
    
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5 #이게 뭔지 정확히 모르겠음
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """
    
    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request, 
        "rooms/search.html", {"city": city, "countries":countries, "room_types": room_types}
        )
