from django.shortcuts import render

def index(request):
    context = {
        'judul':'praxis academy',
        'subjudul':'selamat datang',
    }
    return render(request,'index.html',context)
