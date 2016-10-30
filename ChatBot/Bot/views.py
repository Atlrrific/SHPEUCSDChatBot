from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("My name is Atl and I am the Code Project team lead. ")
