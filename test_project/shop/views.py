from datetime import datetime
from django.db.models import Q

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

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


class ShopAPIList(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request):
        street = request.GET.get("street")
        city = request.GET.get("city")
        open = request.GET.get("open")
        time_now = datetime.now().strftime('%H:%M')

        response = Shop.objects.all()
        if city:
            response = response.filter(city__name=city).values()
        if street:
            response = response.filter(street__name=street).values()
        if open:
            if int(open):
                response = response.filter(Q(time_open__lt=time_now) & Q(time_close__gt=time_now)).values()
            elif int(open) == 0:
                response = response.filter(Q(time_open__gt=time_now) | Q(time_close__lt=time_now)).values()

        if city or street or open:
            return Response({'shop': response})

        return Response({'shop': Shop.objects.all().values()})


class ShopsAPIList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
