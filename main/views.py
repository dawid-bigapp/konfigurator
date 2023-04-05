from django.shortcuts import render

def home(request):
    return render(request, './main/index.html', {})

def uklad(request):
    return render(request, './main/uklad.html', {})

def szyna(request):
    return render(request, './main/szyna.html', {})

def kolor(request):
    return render(request, './main/kolor.html', {})

def wymiary(request):
    return render(request, './main/wymiary.html', {})