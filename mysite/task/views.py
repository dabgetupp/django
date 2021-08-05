from django.shortcuts import render


# Create your views here.

def index(req):   
    if req.POST:
            yourname = req.POST['name']
            print(yourname)
            yourpassword = req.POST['password']
            print(yourpassword)
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')
