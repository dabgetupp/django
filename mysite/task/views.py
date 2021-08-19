from django.shortcuts import redirect, render
from . import models
import psycopg2



# Create your views here.
def index(req):
    conn = psycopg2.connect(
        host="localhost",
        database="task",
        user="postgres",
        password="1qaz"
        )

    curr = conn.cursor()
    cur.callproc('task', (id))
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()

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
    



