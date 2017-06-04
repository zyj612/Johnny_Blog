#同级模块前面要加个点
from django.contrib import admin
from .models import *
# Register your models here.

#注册admin的几个模块
#自定义需要显示的类在下面register里面要重新注册
class ArticleAdmin(admin.ModelAdmin):
#这是后台需要显示的字段名,如果使用exclude就是去除了被选中以外的三个字段都显示
    list_display =('title', 'desc','click_count','date_publish','category',)
    fieldsets = (
        ('基本设置', {
            'fields': ( 'title', 'desc','content','click_count','user',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('category', 'tag'),
        }),
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','nickname','content')
    '''
    fieldsets = 
( {
            'fields': ( 'title', 'desc','content','click_count','user',)
        }),
        '''

#具体作用,注册这些模型
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(CommentReply)

