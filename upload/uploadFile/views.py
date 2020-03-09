from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import ProfileImageForm
from django.core.paginator import Paginator
from .models import ProfilImage

def ProfilImageView(request):
    form = ProfileImageForm(request.FILES or None)
    
    if request.FILES.get('image') != None:
        ProfilImage.objects.create(
            image = request.FILES.get('image')
        )
    context = {
        'form':form
    }

    return render(request, 'uploadFile/index.html', context)

def result(request):
    data = ProfilImage.objects.all()
    paginator = Paginator(data, 3)
    page = request.GET.get('page', 1)

    pagination = paginator.page(page)
    context = {
        'data':data,
        'pagination':pagination,
    }

    return render(request, 'uploadFile/result.html', context)
