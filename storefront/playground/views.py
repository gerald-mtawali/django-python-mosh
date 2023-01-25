# The request handler module
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your models here.
def say_hello(request): 
    return HttpResponse("Hello from a galaxy far away")
