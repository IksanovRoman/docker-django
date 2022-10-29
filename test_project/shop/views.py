import json

from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from shop.models import *
from shop.serializers import ShopSerializer


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

class ShopAPIList(generics. CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopsAPIList(generics. ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer