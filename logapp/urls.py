#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/2/10 10:03
# @Author : hld
# @File : urls.py
# @Software: PyCharm
from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns=[
    path(r'index/', views.index,name='index'),
    path(r'login/', views.login,name='login'),
    path(r'register/', views.register,name='register'),
    path(r'logout/', views.logout,name='logout'),
    url(r'^captcha', include('captcha.urls'))  # 增加这一行
]
