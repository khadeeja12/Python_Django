from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x=calculate()
    return render(request,'hello.html',{'name':'khadeeja'})

def home(request):
    return HttpResponse("Welcome to the homepage!")

def calculate():
    x=1
    y=2
    return x