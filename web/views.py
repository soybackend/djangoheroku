from django.views.generic import ListView
from .models import Persona


class IndexView(ListView):
    model = Persona