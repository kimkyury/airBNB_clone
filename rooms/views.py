from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models



class HomeView(ListView): # Lendering 할 필요가 없어졌음
    
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5 #이게 뭔지 정확히 모르겠음
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
