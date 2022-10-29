from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from shop.models import *


def index(request):
    return render(request, 'shop/base.html')


def show_city(request):
    cities = City.objects.all()

    return render(request, 'shop/city.html', {'cities': cities})


def show_city_id(request, city_id):
    city = City.objects.get(pk=city_id)
    return render(request, 'shop/city.html', {'city': city})


def show_city_street(request, city_id):
    street = Street.objects.filter(city=city_id)
    city = City.objects.get(pk=city_id)

    context = {
        'street': street,
        'city': city,
    }

    return render(request, 'shop/city.html', context=context)


