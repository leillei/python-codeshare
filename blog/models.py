from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from mdeditor.fields import MDTextField


# ----------基础模块----------- #
class Image(models.Model):
    """图片"""
    image = models.ImageField(verbose_name='图片', upload_to='uploads/%Y/%m')
    type_of_user_icon = models.BooleanField(verbose_name='是否为头像', default=False)

    class Meta:
        verbose_name = '图片信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image.name


class User(AbstractUser):
    """用户信息"""
    icon = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name='用户头像', blank=True, null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Category(models.Model):
    """博客分类"""
    name = models.CharField(verbose_name='文档分类', max_length=20, unique=True, default='')

    class Meta:
        verbose_name = '文档分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TagProfile(models.Model):
    """标签"""
    name = models.CharField(verbose_name='标签名', max_length=20, unique=True)

    class Meta:
        verbose_name = '标签名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class InfoMsg(models.Model):
    """网站通知"""
    info = models.CharField(verbose_name='通知内容', unique=True, default='', max_length=100)
    display = models.BooleanField(verbose_name='是否展示', default=True)

    class Meta:
        verbose_name = '通知信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.info


# -----------核心模块------------- #
class Blog(models.Model):
    """博客文章"""
    title = models.CharField(verbose_name='标题', max_length=100, default='', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', default='')
    password = models.CharField(verbose_name='访问密码', max_length=256, default='0')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='文章分类')
    tags = models.ManyToManyField(TagProfile, verbose_name='标签')
    image = models.ForeignKey(Image, verbose_name='封面', on_delete=models.SET_NULL, null=True, blank=True)

    digest = models.TextField(verbose_name='摘要', default='', max_length=300)
    content = MDTextField(verbose_name='内容')

    read_num = models.IntegerField(verbose_name='阅读数', default=0)
    comment_num = models.IntegerField(verbose_name='评论数', default=0)
    approval_num = models.IntegerField(verbose_name='点赞数', default=0)
    pub_date = models.DateTimeField(verbose_name='发表时间', default=datetime.now)
    display = models.BooleanField(verbose_name='是否展示', default=True)

    class Meta:
        verbose_name = '博客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Visitor(models.Model):
    """访客信息"""
    ip = models.CharField(verbose_name='IP地址', max_length=30, unique=True)
    city = models.CharField(verbose_name='城市', default='', max_length=50)
    coordination = models.CharField(verbose_name='经纬度', default='', max_length=50)
    times = models.IntegerField(verbose_name='访问次数', default=0)
    approval_blog_list = models.ManyToManyField(Blog, verbose_name='已赞文章')

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class Comment(models.Model):
    """博客评论"""
    user = models.ForeignKey(User, verbose_name='评论用户', on_delete=models.CASCADE, default='')
    blog = models.ForeignKey(Blog, verbose_name='评论文章', on_delete=models.CASCADE, default='')
    content = models.TextField(verbose_name='评论内容', default='', max_length=1000)
    pub_date = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    is_informed = models.BooleanField(verbose_name='是否通知', default=True)
    parent = models.ForeignKey('self', verbose_name='父评论', on_delete=models.CASCADE, null=True, blank=True)
    display = models.BooleanField(verbose_name='是否展示', default=True)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    """留言"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', default='')
    title = models.CharField(verbose_name='标题', default='', max_length=30)
    content = models.TextField(verbose_name='留言', default='', max_length=1000)
    pub_date = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    is_informed = models.BooleanField(verbose_name='回复通知', default=True)
    display = models.BooleanField(verbose_name='是否展示', default=True)
    reply_content = models.TextField(verbose_name='留言回复', default='', max_length=500)
    is_replied = models.BooleanField(verbose_name='是否已通知', default=False)

    class Meta:
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Resource(models.Model):
    """留言"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', default='')
    title = models.CharField(verbose_name='标题', default='', max_length=30)
    content = models.TextField(verbose_name='内容', default='', max_length=1000)
    pub_date = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    password = models.CharField(verbose_name='访问密码', default='0', max_length=128)
    category = models.CharField(verbose_name='类别', default='', max_length=20)
    link = models.CharField(verbose_name='链接', default='', max_length=200)
    image = models.ForeignKey(Image, verbose_name='图片', null=True, blank=True, on_delete=models.SET_NULL)
    display = models.BooleanField(verbose_name='是否展示', default=True)

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FriendLink(models.Model):
    """友情链接"""
    name = models.CharField(verbose_name='名称', default='', max_length=50)
    url = models.URLField(verbose_name='URL地址', default='', max_length=100)
    description = models.CharField(verbose_name='描述信息', default='', max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    display = models.BooleanField(verbose_name='是否展示', default=True)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
