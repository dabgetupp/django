from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' :'blog',
        'subjudul' :'ini adalah blog praxis academy',
    }
    return render(request,'blog/index.html',context)