from django.shortcuts import render
from .forms import wymiaryOdcinek, wymiaryL, wymiaryU, wymiaryProstokat, wymiaryPodwojneL, wymiarySufitSciana
from django.http import HttpResponseRedirect


ledy = {
    'zabudowa':'',
    'uklad':'',
    'szyna':'',
    'kolor':'',
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'oprawa':'',
    'zaslepki': 0,
    'zasilacze': 0,
    'laczniki': 0,
}

def home(request):
    return render(request, './main/index.html', {})

def uklad(request):
    if request.method == "POST":
        ledy['zabudowa'] = request.POST.get('btnn')
    return render(request, './main/uklad.html', {'ledy':ledy})

def szyna(request):
    if request.method == "POST":
        ledy['uklad'] = request.POST.get('btnn')
    return render(request, './main/szyna.html', {'ledy':ledy})

def kolor(request):
    if request.method == "POST":
        ledy['szyna'] = request.POST.get('btnn')
    return render(request, './main/kolor.html', {'ledy':ledy})

def wymiary(request):
    form1 = wymiaryOdcinek()
    form2 = wymiaryL()
    form3 = wymiaryU()
    form4 = wymiaryProstokat()
    form5 = wymiaryPodwojneL()
    form6 = wymiarySufitSciana()
    if request.method == "POST":
        ledy['kolor'] = request.POST.get('btnn')
    if ledy['uklad'] == "Prosty odcinek":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form1})
    if ledy['uklad'] == "Kształt L":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form2})
    if ledy['uklad'] == "Kształt U":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form3})
    if ledy['uklad'] == "Prostokąt":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form4})
    if ledy['uklad'] == "Podwójne L":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form5})
    if ledy['uklad'] == "L sufit - ściana":
        return render(request, './main/wymiary.html', {'ledy':ledy, 'form':form6})
    
def oprawy(request):
    if request.method == "POST":
        if ledy['uklad'] == "Prosty odcinek":
            form = wymiaryOdcinek(request.POST)
            ledy['a'] = request.POST['wymiara']
        if ledy['uklad'] == "Kształt L":
            form = wymiaryL(request.POST)
            ledy['a'] = request.POST['wymiara']
            ledy['b'] = request.POST['wymiarb']
        if ledy['uklad'] == "Kształt U":
            form = wymiaryU(request.POST)
            ledy['a'] = request.POST['wymiara']
            ledy['b'] = request.POST['wymiarb']
            ledy['c'] = request.POST['wymiarc']
        if ledy['uklad'] == "Prostokąt":
            form = wymiaryProstokat(request.POST)
            ledy['a'] = request.POST['wymiara']
            ledy['b'] = request.POST['wymiarb']
        if ledy['uklad'] == "Podwójne L":
            form = wymiaryPodwojneL(request.POST)
            ledy['a'] = request.POST['wymiara']
            ledy['b'] = request.POST['wymiarb']
            ledy['c'] = request.POST['wymiarc']
            ledy['d'] = request.POST['wymiard']
        if ledy['uklad'] == "L suit - ściana":
            form = wymiarySufitSciana(request.POST)
            ledy['a'] = request.POST['wymiara']
            ledy['b'] = request.POST['wymiarb']
    return render(request, './main/oprawy.html', {'ledy':ledy})


def podsumowanie(request):
    if request.method == "POST":
        ledy['oprawa'] = request.POST.get('btnn')
        dlugoscszynya = int(ledy['a'])
        dlugoscszynyb = int(ledy['b'])
        dlugoscszynyc = int(ledy['c'])
        dlugoscszynyd = int(ledy['d'])
        ile2a = 0
        ile1a = 0
        ile2b = 0
        ile1b = 0
        ile2c = 0
        ile1c = 0
        ile2d = 0
        ile1d = 0
        while dlugoscszynya > 0:
            if dlugoscszynya > 0 and dlugoscszynya <= 1:
                ile1a += 1
                dlugoscszynya -= 1
            elif dlugoscszynya > 0 and dlugoscszynya > 1:
                ile2a += 1
                dlugoscszynya -= 2
        while dlugoscszynyb > 0:
            if dlugoscszynyb > 0 and dlugoscszynyb <= 1:
                ile1b += 1
                dlugoscszynyb -= 1
            elif dlugoscszynyb > 0 and dlugoscszynyb > 1:
                ile2b += 1
                dlugoscszynyb -= 2
        while dlugoscszynyc > 0:
            if dlugoscszynyc > 0 and dlugoscszynyc <= 1:
                ile1c += 1
                dlugoscszynyc -= 1
            elif dlugoscszynyc > 0 and dlugoscszynyc > 1:
                ile2c += 1
                dlugoscszynyc -= 2
        while dlugoscszynyd > 0:
            if dlugoscszynyd > 0 and dlugoscszynyd <= 1:
                ile1d += 1
                dlugoscszynyd -= 1
            elif dlugoscszynyd > 0 and dlugoscszynyd > 1:
                ile2d += 1
                dlugoscszynyd -= 2                
        ile2 = ile2a + ile2b + ile2c + ile2d
        ile1 = ile1a + ile1b + ile1c + ile1d
        if ledy['uklad'] == "Prosty odcinek":
            ledy['zaslepki'] = 2
        if ledy['uklad'] == "Kształt L":
            ledy['zaslepki'] = 2
            ledy['laczniki'] = 1
        if ledy['uklad'] == "Kształt U":
            ledy['zaslepki'] = 2
            ledy['laczniki'] = 2
        if ledy['uklad'] == "Prostokąt":
            ledy['laczniki'] = 4
        if ledy['uklad'] == "Podwójne L":
            ledy['zaslepki'] = 4
            ledy['laczniki'] = 2
        if ledy['uklad'] == "L suit - ściana":
            ledy['zaslepki'] = 2
            ledy['laczniki'] = 1
    return render(request, './main/podsumowanie.html', {'ledy':ledy, 'ile1':ile1, 'ile2':ile2})
