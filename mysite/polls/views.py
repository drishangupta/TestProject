from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='background-color: yellow;'>Helloooo, world. You're at the polls index.</h1>")