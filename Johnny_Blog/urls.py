# -*- coding: utf-8 -*-
"""Johnny_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import viewsa
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.views import static
from Blog import views as index_view


urlpatterns = [
    #(?P<name>..)这个正则表达式是分组的意思,name代表他的别名可以重复使用
    #这里又是一个坑1.10的django引用方法和之前的版本不一样了
    #在django1.10版本中views视图函数的语法出现了变化，需要先导入views视图函数，然后再引用其内部的函数，同时去掉双引号
    #z这里有两个static
    url(r'^uploads/(?P<path>.*)$',static.serve,{"document_root":settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^$',index_view.index,name='home'),
    url(r'^archive/$',index_view.archive,name='archive'),
    url(r'^comment/$',index_view.comment_post, name='comment_post'),
    url(r'^comment_reply/$',index_view.comment_reply, name='comment_reply'),
    url(r'^comment_reply_child/$',index_view.comment_reply_child, name='comment_reply_child'),
    url(r'^article/$',index_view.article,name='article'),
    url(r'^category_articles/$',index_view.category_articles,name='category_articles'),
    url(r'^register/$',index_view.blog_register,name='register'),
    url(r'^login/$',index_view.blog_login,name='login'),
    url(r'^logout/$',index_view.blog_logout,name='logout'),
    url(r'^userinfo/$',index_view.get_userinfo,name='userinfo'),
    url(r'^updateuser/$',index_view.updateUser,name='updateUser'),
    url(r'^usercheck/$',index_view.username_check,name="userNameCheck"),
    url(r'^aboutblog/$',index_view.aboutBlog,name="aboutblog"),
    url(r'^praise/$',index_view.countPraise,name="countPraise"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
