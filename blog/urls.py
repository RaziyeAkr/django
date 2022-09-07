from django.urls import path
from .views import ArticleList , ArticleDetail , CategoryList

app_name="blog"

urlpatterns=[
    path('',ArticleList.as_view(), name="home"),
    path('page/<int:page>',ArticleList.as_view(), name="home"),
    path('article/<slug:slug>',ArticleDetail.as_view() , name='detail'),
    path('category/<slug:slug>',CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>',CategoryList.as_view() , name='category'),
]