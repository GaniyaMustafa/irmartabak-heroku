from django.shortcuts import render
from database import models as m


def index(request):
    makanan = m.martabakhome.objects.all()
    context = {
        'martabak' : makanan,
    }
    return render(request, 'index.html', context)