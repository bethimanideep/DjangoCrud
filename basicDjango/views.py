from django.shortcuts import render
from django.http  import HttpResponse
def enter(request,username):
    print(username)
    return HttpResponse("Hello "+username+"")
def leave(request,username):
    return HttpResponse("Bye "+username+"")
    
# Create your views here.
