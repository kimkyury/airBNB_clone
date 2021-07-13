from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):  # Lendering 할 필요가 없어졌음


    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5 #이게 뭔지 정확히 모르겠음
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
