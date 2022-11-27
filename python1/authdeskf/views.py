from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Всем здравствуйте')
# Create your views here.
