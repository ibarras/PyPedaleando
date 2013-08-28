from django.shortcuts import render
from polls.models import Poll, Choice

# Create your views here.

"""
Mostramos todas las encuestas
"""
def pollsMain(request):
    template = "encuestas.html"
    encuestas_listado = Poll.objects.all().order_by("-pub_date")
    return render(request, template, locals())

