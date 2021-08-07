from django.shortcuts import redirect, render
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
    currentData = models.tugas.objects.filter(pk=id)
    if request.POST:
        new_name = request.POST['username']
        currentData.update(name = new_name)
        return redirect('/')

    return render(request, 'update.html', {
        'current_name' : currentData.first().name
    })

def delete(request, id):
        models.tugas.objects.filter(pk=id).delete()
        return redirect('/')
    



