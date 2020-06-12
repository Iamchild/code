#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 下午2:49
# @Author  : ZhiLin
# @Email   : happylin1015@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from . import views
import json

# app_name：应用姓，被用作当前应用路由别名的姓
app_name = 'user'

urlpatterns = [
    # 请求路径：http://127.0.0.1:8000/users/index/
    path('index/', views.index_view, name='index'),
    re_path('^say/$', views.say_view, name='say'),
    re_path('^sayhello/$', views.sayhello_view, name='sayhello'),

]