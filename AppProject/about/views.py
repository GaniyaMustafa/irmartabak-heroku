from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'about.html')

def detail(request):
    return HttpResponse('<h1>ini detail about</h1>')