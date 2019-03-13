from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index/', views.Index.as_view(), name='index'),
    path('article/category/<str:name>/<int:page>/', views.Articles.as_view(), name='article_category'),
    path('article/tag/<str:name>/<int:page>/', views.Articles.as_view(), name='article_tag'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('search/<int:page>/', views.Search.as_view(), name='search'),
    path('archive/<int:year>/<int:month>/<int:page>/', views.Archive.as_view(), name='archive'),
    path('message/<int:page>/', views.MessageInfo.as_view(), name='message'),
    path('about/', views.About.as_view(), name='about'),
    path('approval/', views.Approval.as_view(), name='approval'),
    path('friendlink/', views.ApplyFriendLink.as_view(), name='friend_link'),
    path('resource/<int:page>/', views.ResourceInfo.as_view(), name='resource'),
    
]
