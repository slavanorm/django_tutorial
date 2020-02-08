from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<hr>Privet <br><strong>Lev</strong>")
