from django.shortcuts import render,redirect
from .models import Person
import datetime

all= Person.objects.all()
def khooneh(request):
    return render(request,'home.html',{'name' : 'adminjoon','time':datetime.datetime.now()})
def say_hello(request):
    return render(request,'hello.html')
def contact(request):
    return render(request,'contact.html',{'contactall':all})
def detail(request,Person_id):
    return render(request,'detail.html',{'ghavam':Person.objects.get(id=Person_id)})
def delete(request,Person_id):
    Person.objects.get(id=Person_id).delete()
    return redirect('contact')