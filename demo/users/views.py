from django.shortcuts import render
from django.http import HttpResponse
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
    return HttpResponse("itcast V1.0")
