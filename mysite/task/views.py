from django.shortcuts import render
from . import models


# Create your views here.

def index(request):   
    data = models.tugas.objects.all()
    contoh ="welcome back"
    if request.POST:
        input_nama = request.POST['name']
        models.tugas.objects.create(name=input_nama)
        data = models.tugas.objects.all()
    return render(request, 'index.html', {
        'data': data,
    })

def about(req):
    return render(req, 'about.html')

def update(request, id):
    if request.POST:
        newname = request.POST['username']
        models.tugas.objects.filter(pk=id). update(name=new_name)
        redirect('/')
    return render(request, 'index.html',{
        'data': data,
    })

def delete(request, id):
    return render(request, 'index.html',{
        'data': data,
    })



