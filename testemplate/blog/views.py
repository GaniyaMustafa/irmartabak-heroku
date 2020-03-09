from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail/detailblog.html')