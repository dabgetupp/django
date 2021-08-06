from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' :'about',
        'subjudul' :'ini adalah tentang kita bersama',
    }    
    return render(request, 'about/index.html', context)


