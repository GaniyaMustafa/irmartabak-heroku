from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Templates_variabel',
        'subjudul':'Halaman Blog',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
        ]
    }
    return render(request, 'index.html', context)
