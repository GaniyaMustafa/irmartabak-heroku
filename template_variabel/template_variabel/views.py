from django.shortcuts import render

def index(request):
    context = {
        'judul':'Template_Variable',
        'subjudul':'Halaman Index',
        'nav': [
            ['/', 'Home'],
            ['/blog/', 'Blog']
        ]
    }
    return render(request, 'index.html', context)

