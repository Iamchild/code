#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 下午5:13
# @Author  : ZhiLin
# @Email   : happylin1015@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from . import views
# 请求路径：weather/shanghai/2020
# -------Django的路由分发-------
# re.match(r'weather/([a-zA-Z]+)/(\d{4}/)'
urlpatterns = [
    # path('weather/', views.weather_view)
    re_path(r'weather/(?P<city>[a-zA-Z]+)/(?P<year>\d{4})/', views.weather_view)

]
