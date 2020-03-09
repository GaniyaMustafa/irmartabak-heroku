from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog.html")

def detail(request):
    return HttpResponse('<h1>Ini detail blog</h1>')
