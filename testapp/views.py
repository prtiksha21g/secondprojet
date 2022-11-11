from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class HttpResoonse:
    pass


def view(request):
    return  HttpResoonse(request,'index.html')