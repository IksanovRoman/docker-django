from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('city/', show_city, name='show_city'),
    path('city/<int:city_id>', show_city_id, name='show_city_id'),
    path('city/<int:city_id>/street/', show_city_street, name='show_city_street'),
    path('shop/', ShopAPIList.as_view()),
    path('shops/', ShopsAPIList.as_view()),
    ]
