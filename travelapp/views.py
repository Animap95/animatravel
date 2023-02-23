from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Place,People

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj1})