from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
"""
1、定义视图函数
2、路由映射
"""
# 视图函数，本质就是一个函数
# 该函数的定义，必须遵循Django框架的约定

# 定义视图函数
# 1、业务功能自己实现
# 2、视图函数的参数，必须遵循Django的约定
# 3、视图函数必须遵循Django约定


def index_view(request):
    """
    :param request: 请求对象，在Django调用该函数的时候自动传入的
    :return:一个响应对象--响应对象里面封装动态数据
    """
    # 实现功能

    # 使用路由别名，反向解析出路由对象
    url = reverse('user:say')

    # 外部重定向
    # return redirect('https:www.baidu.com')
    # 内部重定向
    return redirect(url)
    # return HttpResponse("请求体数据！")


# /users/say
def say_view(request):
    """
    :param request:
    :return:
    """
    # 该视图函数中，使用request请求对象，提取请求参数

    # 1、提取请求的查询字符串参数
    # GET属性是一个QueryDict类型（多值字典，一键多值）
    print(request.GET)
    print('name:', request.GET.get('name'))
    print('age:', request.GET.get('age'))
    # 取一个key的所有值
    print("所有age", request.GET.getlist('age'))
    return HttpResponse('say')


# /users/sayhello
def sayhello_view(request):
    return HttpResponse('say hello')
