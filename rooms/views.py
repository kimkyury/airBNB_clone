from django.views.generic import ListView, DetailView
from django.shortcuts import render
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
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
