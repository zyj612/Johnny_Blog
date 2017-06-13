# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField

# Create your models here.

# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
#兼容python2
@python_2_unicode_compatible
#继承了系统自带的user
class User(AbstractUser):
    #%Y和%m代表的是年和月
    #设置头像的上传路劲
    avatar = models.ImageField(upload_to='avatar', default='uploads/avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户昵称')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

#Meta主要是定义Django模型类的行为属性，比如下面的verbose_name就是给这个模型类添加了一个名称
#还有其他的具体属性
    class Meta:
        verbose_name = '分类'
#这个选项是指定模型的复数形式是什么
        verbose_name_plural = verbose_name
#这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的，这里的id是系统自带的
        ordering = ['index', 'id']

    def __str__(self):
        return self.name

# 自定义一个文章Model的管理器
# 1、新加一个数据处理的方法
# 2、改变原有的queryset
class ArticleManager(models.Manager):
    #主要目的是获取同意日期下所对应的文章总数
    def distinct_date(self):
        distinct_date_list = []#用来保存结果
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m')#转换格式
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list
    #获取文章总数，用在文章详情中(目前为止想到的折中办法)
    def last_article(self):
        id_list = self.values('id')
        last_article_id = 0
        for id in id_list:
            if(id):
                last_article_id=last_article_id+1
        return last_article_id


# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    #content = models.TextField(verbose_name='文章内容')

    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    click_count = models.IntegerField(default=0, verbose_name='阅读次数')
    praise_count = models.IntegerField(default=0, verbose_name='点赞总数')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    #ForeignKey是多对一，ManyToManyField是多对多，这里的多对一是指该字段
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    #绑定到Tag类中
    tag = models.ManyToManyField(Tag, verbose_name='标签')
#使用自定义的Manager
    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户昵称')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    avatar = models.ImageField( default='uploads/avatar/default.png', max_length=200, blank=True,null=True, verbose_name='用户头像')
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

#回复评论
class CommentReply(models.Model):
    #这是回复评论.
    # 将二级评论关联对应的一级评论
    nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户昵称')
    content = models.TextField(verbose_name='回复内容')
    comment = models.ForeignKey(Comment, related_name='comment_replies')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    user = models.ForeignKey(User, related_name='user_comment_replies', null=True, blank=True,
                               on_delete=models.SET_NULL)
    reply_to_user = models.ForeignKey(User, related_name='user_replied', null=True, blank=True, on_delete=models.SET_NULL)
    reply_to_nickname = models.CharField(max_length=30, blank=True, null=True, verbose_name='回复的用户昵称')
    date_reply = models.DateTimeField(auto_now_add=True, verbose_name='回复评论时间')
    state = models.CharField(max_length=64, null=True, blank=True)
    comment_child = models.CharField(max_length=10, blank=True, null=True, verbose_name='回复了哪条子评论')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    avatar = models.ImageField(default='uploads/avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    class Meta:
        verbose_name = '回复评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}->{1}'.format(self.nickname, self.reply_to_nickname)

# 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title

#统计点赞的表,表中的id是自己自动增加的
class UserPraises(models.Model):
    article = models.ForeignKey(Article,verbose_name="文章")
    total_praise = models.CharField(max_length=10,verbose_name="累计总数")
    user_ip = models.CharField(max_length=20,verbose_name="用户IP地址")
    praise_date = models.DateTimeField(auto_now_add=True,verbose_name="点击时间")



