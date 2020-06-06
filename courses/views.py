from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    x="<h1>Welcome to Django framework</h1>"
    return HttpResponse(x)


