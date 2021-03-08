# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import models

# Create your views here.


def home(request):
    return render(request, "home.html")


def book_list(request):
    book_queryset = models.Book.objects.all()
    return render(request, "book_list.html", locals())


def book_add(request):
    if request.method=='POST':
        # 获取所有的数据
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('authors')
        # 书籍表添加数据
        book_obj = models.Book.objects.create(title=title,price=price,publish_date=publish_date,publish_id=publish_id)
        # 增加绑定关系
        book_obj.authors.add(*author_list)
        # 跳转书籍展示页面
        return redirect("book_list")

    # 查询数据并返回
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, "book_add.html", locals())

