import os
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
import json as simplejson
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from pip import logger

from Blog.models import Article, Category, Comment, CommentReply, User
from django.core.paginator import Paginator, EmptyPage,InvalidPage,PageNotAnInteger
from .custome_pythoncode import extendpaginator
from django.db import connection

#设置全局的变量,项目中任何一张网页都可以使用的
def global_content(request):
    #使用自定管理器中的方法,可以单独处理某个字段
    archive_date = Article.objects.distinct_date()
    #用来做上下页的
    last_article_id= Article.objects.last_article()
    #获取文章的所有种类
    article_category = Category.objects.all()
    articles= Article.objects.all()[:10]
    cursor = connection.cursor()
    cursor.execute("(SELECT nickname,avatar,content ,id as comment_id ,article_id,user_id,date_publish as date_order FROM blog_comment) UNION (SELECT nickname,avatar,content,comment_id,article_id,user_id,date_reply as date_order FROM blog_commentreply) order by date_order desc LIMIT 10;")

    last_comments =cursor.fetchall()



    '''
    for a in archive_date:
        print (a)
    '''
    return locals()
# Create your views here.
#测试用的，遍历一个object的所有属性
def prn_obj(obj):
    print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
def index(request):
    try:
        #查询所有文章的结果集
        #把结果集传递给分页类，10指的是每页最多有几条记录
        #这里是把文章结果集传过来，每页只显示5条结果
        #  prn_obj(article_list)打印类中的所有属性
        article_list  = Article.objects.all()#获取文章总数
        article_list_all = Article.objects.all()[:6]#首页显示的最新文章数
        Article.objects.distinct_date()
        article_list = page_pagionation(request,article_list)
    except Exception as e:
        print (e)
    return render(request ,'index.html',{'Article_list':article_list,'Article_list_all':article_list_all})
    #return render(request, 'index.html', locals())


def archive(request):
    try:
        year = request.GET.get('year',None)#如果取不到值则用none
        month= request.GET.get('month',None)
        archive_list = Article.objects.filter(date_publish__icontains= year+'-'+month)#利用模糊查询把2017年5月的文章都找出来
        archive_list = page_pagionation(request,archive_list)
        #print (archive_list_id)
    except Exception as e:
        logger.error(e)
    return render(request,'archive.html',locals())

def category_articles(request):
    try:
        #这里获取的是category里面的id
        category = request.GET.get('category',None)
        category_articles = Article.objects.filter(category=category)
        #在article表中的category对应Category表中的id字段
        category_name = Category.objects.get(pk=category)
    except Exception as e:
        logger.error(e)
    return render(request,'category_articles.html',locals())

def article(request):
    try:
        id = request.GET.get('id',None)
        #这里是当提交的参数为空的时候，也会跳转错误
        if(id=="") or id==None:
            id = 0
        pre = int(id)-1
        next =int(id)+1
        try:
            #精确查询,这里的id是字符串类型
            article=Article.objects.get(pk=id)
            print(article.id)
            #get匹配一条结果，filter匹配多条结果
            comments = Comment.objects.filter(article_id=article.id).order_by('date_publish')
            comment_list=comments_pagionation(request,comments)
            print('xxxx')
            print(comment_list.paginator.num_pages)
        except Article.DoesNotExist:
            return render(request,'failure.html',{'reason':'文章不存在'})
    except Exception as e:
        logger.error(e)
    return render(request,'article.html',locals())




def page_pagionation(request,article_list):
    try:
        #自定义的分页器，初始化一页的文章总数为1,可以客制化
        paginator = extendpaginator.extendPaginator(article_list, 5)
        # 获取客户端提交的request,因为一开始get请求的'page’是不存在的,然后设置默认为第一页.
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
        # 如果页码不是整数或者无效页码抛出异常
    except (PageNotAnInteger, InvalidPage):
        article_list = paginator.page(1)
        # 如果页码为空，返回最后一页

    except EmptyPage:
        # paginator.num_pages(代表最大分页数)
        article_list = paginator.page(paginator.num_pages)
        # 文章归档
        #1.获取文章的发表日期
        # 方法不适用，Article.object.values('date_publish').distinct()
        # cursor = connection.cursor()
        # cursor.execute("SELECT DISTINCT DATE_FORMAT(date_publish,'%y-%m') from blog_article")
        # row = cursor.fetchall()
        # print (row)
        # 直接使用sql语句不推荐
    return article_list


def comment_post(request):
    try:
        #这里像数据库写数据等号赋值之间不能有空格,函数中的变量吗必须小写
        if request.method == "POST":
            nickname = request.POST['NickName']
            useremail = request.POST['BEmail']
            cmtcontent = request.POST['CmtText']
            articleid  = request.POST['CmtArtId']
            userid = request.POST['UserId']
            User.objects.get(pk=userid)
            comment = Comment.objects.create(nickname=nickname,
                                             email=useremail,
                                             content=cmtcontent,
                                             article_id=articleid,
                                             user_id = userid,)
            comment.save()
    except Exception as e:
        logger.error(e)
    #重定向到当前地址
    return redirect(request.META['HTTP_REFERER'])


def comment_reply(request):
    try:
        # 这里像数据库写数据等号赋值之间不能有空格,函数中的变量吗必须小写
        #用户只有nickname没有user_id的时候，所以不一定向数据库中保存
        if request.method == "POST":
            print('xxx')
            nickname = request.POST['NickName']
            useremail = request.POST['BEmail']
            rpycontent = request.POST['CmtText']
            parentcomment = request.POST['ParentComment']
            request.POST['UserId']
            userid =request.POST['UserId']
            replyto_nickname = request.POST['ReplyTo']
            cmtartid = request.POST['CmtArtId']
            #这里是回复顶级评论的时候
            user = Comment.objects.get(pk =request.POST['ParentComment'] )
            user = user.user_id
            commentreply = CommentReply.objects.create(nickname=nickname,
                                             email=useremail,
                                             content=rpycontent,
                                             comment_id=parentcomment,
                                            # 草草草草草，居然是个字符0.
                                             user_id=userid if userid !="0" else None,
                                            article_id = cmtartid,
                                            reply_to_nickname = replyto_nickname,
                                            reply_to_user_id =user)
            commentreply.save()
    except Exception as e:
        logger.error(e)
    # 重定向到当前地址
    return redirect(request.META['HTTP_REFERER'])




def comment_reply_child(request):
    try:
        # 这里像数据库写数据等号赋值之间不能有空格,函数中的变量吗必须小写
        #用户只有nickname没有user_id的时候，所以不一定向数据库中保存
        if request.method == "POST":
            nickname = request.POST['NickName']
            useremail = request.POST['BEmail']
            rpycontent = request.POST['CmtText']
            userid = request.POST['UserId']
            cmtartid = request.POST['CmtArtId']
            print(cmtartid)
            #这里是回复顶级评论的时候
            user = CommentReply.objects.get(pk =request.POST['ParentComment'] )
            #回复具体那条子评论的id
            reply_to_user_id = user.user_id
            reply_to_user_nickname = user.nickname
            comment_id = user.comment_id

            commentreply = CommentReply.objects.create(nickname=nickname,
                                             email=useremail,
                                             content=rpycontent,
                                             comment_id=comment_id,
                                             user_id=userid if userid !="0" else None,
                                            article_id=cmtartid,
                                            reply_to_nickname = reply_to_user_nickname,
                                            reply_to_user_id =reply_to_user_id)
            commentreply.save()
            print('yyy')
    except Exception as e:
        logger.error(e)
    # 重定向到当前地址
    return redirect(request.META['HTTP_REFERER'])

def comments_pagionation(request,comments):
    try:
        #自定义的分页器，初始化一页的文章总数为1,可以客制化
        paginator = extendpaginator.extendPaginator(comments, 1)
        # 获取客户端提交的request,然后设置默认为第一页
        page = int(request.GET.get('cmt',1))
        comment_list = paginator.page(page)
        # 如果页码不是整数或者无效页码抛出异常
    except (PageNotAnInteger, InvalidPage):
        comment_list = paginator.page(1)
        # 如果页码为空，返回最后一页
    except EmptyPage:
        # paginator.num_pages(代表最大分页数)
        comment_list = paginator.page(paginator.num_pages)
        # 文章归档
        #1.获取文章的发表日期
        # 方法不适用，Article.object.values('date_publish').distinct()
        # cursor = connection.cursor()
        # cursor.execute("SELECT DISTINCT DATE_FORMAT(date_publish,'%y-%m') from blog_article")
        # row = cursor.fetchall()
        # print (row)
        # 直接使用sql语句不推荐
    return comment_list

#注册信息
def blog_register(request):
    try:
        if request.is_ajax():
            username_json = simplejson.loads(request.POST['data'])
            username = username_json['userName']
            password = username_json['password']
            nickname = username_json['nickname']
            email = username_json['email']
            url = username_json['source_url']
            userinfo = User.objects.create(
                    username=username,
                    email=email,
                    url=url,
                    nickname = nickname,
                    # 密码加密
                    password=make_password(password))
            userinfo.save()
                # 登录
            userinfo.backend = 'django.contrib.auth.backends.ModelBackend'# 指定默认的登录验证方式
            login(request, userinfo)
            return HttpResponse("注册成功")
    except Exception as e:
            logger(e)
    return redirect(url)

def blog_login(request):
    try:
        if request.is_ajax():
            print('ajax,ajax')
            #前端直接发送json数据过来
            username_json = simplejson.loads(request.POST['data'])
            username = username_json['userName']
            password = username_json['password']
            rem_status = username_json['rem_status']
            result = {'result': '登陆成功'}
            userinfo = authenticate(username=username, password=password)
            print(userinfo)
            if userinfo is not None:

                    #1.7以后的版本直接使用此方法
                userinfo.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, userinfo)
                if rem_status:
                    #如果记住密码会默认是5小时
                    request.session.set_expiry(60*60*5)
                    settings.SESSION_SAVE_EVERY_REQUEST =False
                    return JsonResponse(result)
                else:
                    settings.SESSION_SAVE_EVERY_REQUEST = True
                    return JsonResponse(result)
            else:
                print("2222222")
                     # 登录
                '''username = request.POST["bomp_username"]
            password = request.POST["bomp_password"]
            url = request.POST['source_url']
            user = authenticate(username=username, password=password)                                  
            '''
                # 指定默认的登录验证方式
                result = {'result': '用户名或密码不正确'}
                return JsonResponse(result)
    except Exception as e:
        logger(e)
    return HttpResponseNotAllowed(['POST'])

def blog_logout(request):
    try:
        logout(request)
    except Exception as e:
        logger.error(e)
    #返回提交请求前的地址
    return redirect(request.META['HTTP_REFERER'])

def get_userinfo(request):
    if request.user.is_authenticated():
        return render(request,'userinfo.html')
    else:
        return render(request,'failure.html',{'reason':'用户信息不存在'})

#更新用户信息,上传头像
def updateUser(request):
    if request.method == 'POST':
        #获取头像文件
        path = os.path.join(settings.MEDIA_ROOT, 'avatar')
        icon = request.FILES.get('file',None)
        avatarfile = os.path.join(path,request.user.username+".png")
        if os.path.isfile(avatarfile):
            print('delete')
            os.remove(avatarfile)
        if icon is not None:
            f = open(os.path.join(path,icon.name), 'wb')
            #写文件操作
            for chunk in icon.chunks():
                f.write(chunk)
            f.close()
            os.rename(f.name,avatarfile)
            relpath = os.path.relpath(avatarfile,settings.BASE_DIR)

            #保存头像文件路径
            User.objects.filter(username=request.user.username).update(avatar = relpath)
            return HttpResponse("上传成功")
        else:
            return HttpResponse("no files for upload!")

#检测用户名是否已经存在
def username_check(request):
    try:
        if request.is_ajax():
            username = request.POST.get('data')
            print(username)
            try:
                User.objects.get(username=username)
                return HttpResponse("用户名已存在")
            except User.DoesNotExist:
                return HttpResponse("notexist")
    except Exception as e:
        logger(e)

def aboutBlog(request):
    return render(request, 'failure.html', {'reason': '关于本站正在开发中'})






