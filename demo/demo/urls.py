"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from users.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # 指定请求路径==>视图函数
    # django进行路径匹配之前，会把请求路径的顶头的根/去掉
    # path('index/',index_view),
    # 在总路由中，只匹配前缀，确定对应的子路由
    # 前缀users/的全部
    path('users/', include('users.urls')),
    path('', include('weather.urls')),
]
