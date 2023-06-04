from django.shortcuts import render
from .models import *


def products(request):
    products =  Products.objects.all().order_by('?')[:1] #the number four is to limit the number of queries shown on the browser from the database. Meaning that only five queries would be shown.
    products2 =  Products.objects.all().order_by('?')[:1]
    products3 =  Products.objects.all().order_by('?')[:1]
    products4 =  Products.objects.all().order_by('?')[:1]
    products5 =  Products.objects.all().order_by('?')[:1]
    products6 =  Products.objects.all().order_by('?')[:1]
    products7 =  Products.objects.all().order_by('?')[:1]
    products8 =  Products.objects.all().order_by('?')[:1]
    products9 =  Products.objects.all().order_by('?')[:1]
    products10 =  Products.objects.all().order_by('?')[:1]
    products11 =  Products.objects.all().order_by('?')[:1]
    products12 =  Products.objects.all().order_by('?')[:1]

    return render(request, 'home.html', {'products':products, 'products2':products2, 'products3':products3, 'products4':products4, 'products5':products5, 'products6':products6,'products7':products7, 'products8':products8, 'products9':products9, 'products10':products10, 'products11':products11, 'products12':products12})

def electronics(request):
    electronics = Electronics.objects.all().order_by('?')[:1]
    electronics2 = Electronics.objects.all().order_by('?')[:1]
    electronics3 = Electronics.objects.all().order_by('?')[:1]
    electronics4 = Electronics.objects.all().order_by('?')[:1]
    electronics5 = Electronics.objects.all().order_by('?')[:1]
    electronics6 = Electronics.objects.all().order_by('?')[:1]
    electronics7 = Electronics.objects.all().order_by('?')[:1]
    electronics8 = Electronics.objects.all().order_by('?')[:1]
    electronics9 = Electronics.objects.all().order_by('?')[:1]
    electronics10 = Electronics.objects.all().order_by('?')[:1]
    electronics11 = Electronics.objects.all().order_by('?')[:1]
    electronics12 = Electronics.objects.all().order_by('?')[:1]

    return render(request, 'electronics.html', {'electronics': electronics, 'electronics2': electronics2, 'electronics3': electronics3, 'electronics4': electronics4, 'electronics5': electronics5, 'electronics6': electronics6, 'electronics7': electronics7, 'electronics8': electronics8, 'electronics9': electronics9, 'electronics10': electronics10, 'electronics11': electronics11, 'electronics12': electronics12})

def accessories(request):
    accessories = Accessories.objects.all().order_by('?')[:4]


    return render(request, 'accessories.html', {'accessories': accessories})


def specific2(request,pk):
    specifics2 = Electronics.objects.filter(id=pk)
    return render(request, 'specifics2.html', {'specifics2':specifics2})

def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Products.objects.filter(item__contains=query_name)
            if not results:
                    return render(request, 'noresults.html')
        return render(request, 'specifics.html', {"results":results})

    return render(request, 'specifics.html')

def search_product2(request):
    """ search function  """
    if request.method == "POST":
        query_name2 = request.POST.get('name', None)
        if query_name2:
            search2 = Electronics.objects.filter(item__contains=query_name2)
            if not search2:
                    return render(request, 'noresults.html')
        return render(request, 'specifics2.html', {"search2":search2})

    return render(request, 'specifics2.html')

def details2(request,pk):
    details2 = Products.objects.filter(id=pk)
    return render(request, 'moredetails2.html', {'details2':details2})

def details(request,pk):
    details = Electronics.objects.filter(id=pk)
    return render(request, 'moredetails.html', {'details':details})






def specific(request,pk):
    specifics = Products.objects.filter(id=pk)
    return render(request, 'specifics.html', {'specifics':specifics})


def admincontact(request):
    return render(request, 'admincontact.html')

def specific3(request):
    specifics3 = Electronics.objects.all()
    return render(request, 'specifics3.html', {'specifics3':specifics3})

def ElJubilazoStore(request):
    jubilazomarket =  ElJubilazo.objects.all().order_by('?')[:1] #the number four is to limit the number of queries shown on the browser from the database. Meaning that only five queries would be shown.


    return render(request, 'ElJubilazo.html', {'jubilazomarket':jubilazomarket,})