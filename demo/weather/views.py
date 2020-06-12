from django.shortcuts import render
from django import http

# Create your views here.


def weather_view(request, city, year):
    print('city:', city)
    print('year:', year)
    return http.HttpResponse('天气！')
