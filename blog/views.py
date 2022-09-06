import re
from django.core.paginator import Paginator
from django.shortcuts import render ,get_object_or_404
from .models import Article ,Category
# Create your views here.
#view of home page
def home(request, page=1):
    articles_list= Article.objects.published()
    paginator= Paginator(articles_list,2)
    articles=paginator.get_page(page)
    context = {
        'articles' : articles,
        
    }

    return render(request , "blog/home.html" , context)
#view of detail for post article
def detail(request , slug):
    context = {
        'article' : get_object_or_404(Article, slug=slug ,status='p'),
    }

    return render(request , "blog/detail.html" , context)
#view of category 
def category(request , slug, page=1):
    category=get_object_or_404(Category, slug=slug ,status=True)
    articles_list=category.articles.published()
    paginator= Paginator(articles_list,2)
    articles=paginator.get_page(page)
    
    context = {
        'category' : category,
        "articles": articles
    }
    return render(request , "blog/category.html" , context)
