from django.contrib import admin

# Register your models here.
from .models import User, Category, TagProfile, Blog, Comment, Message, InfoMsg, Visitor, Image, Resource, FriendLink


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [('文章基本信息', {'fields': ['title', 'author', 'password', 'display', 'category', 'tags', 'image']}),
                 ('文章内容', {'fields': ['digest', 'content']}),
                 ('关联内容', {'fields': ['read_num', 'comment_num', 'approval_num', 'pub_date']})]
    list_display = (
        'title', 'author', 'password', 'display', 'category', 'read_num', 'approval_num', 'comment_num', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'blog', 'is_informed', 'display', 'parent', 'content', 'pub_date']
    list_display = ('user', 'blog', 'display', 'is_informed', 'parent', 'pub_date')


class MessageAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'pub_date', 'display', 'is_informed', 'is_replied', 'content', 'reply_content']
    list_display = ('user', 'title', 'display', 'is_informed', 'is_replied', 'pub_date')


class VisitorAdmin(admin.ModelAdmin):
    fields = ['ip', 'city', 'coordination', 'times', 'approval_blog_list']
    list_display = ('ip', 'city', 'coordination', 'times')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'icon')


class ImageAdmin(admin.ModelAdmin):
    fields = ['image', 'type_of_user_icon']
    list_display = ('image', 'type_of_user_icon')


class ResourceAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'password', 'category', 'link', 'display', 'image', 'content', 'pub_date']
    list_display = ('user', 'title', 'password', 'category', 'display', 'pub_date')


class FriendLinkAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'display', 'description', 'add_time']
    list_display = ('name', 'url', 'display', 'description', 'add_time')


class InfoMsgAdmin(admin.ModelAdmin):
    fields = ['info', 'display']
    list_display = ('info', 'display')


admin.site.register(User, UserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(InfoMsg, InfoMsgAdmin)
admin.site.register(TagProfile)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(FriendLink, FriendLinkAdmin)
