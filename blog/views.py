import re
from django.core.paginator import Paginator
from django.views.generic import ListView ,DetailView
from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.models import User
from .models import Article ,Category
# Create your views here.
#view of home page
class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by =2
#view of detail for post article
class ArticleDetail(DetailView):
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug ,status='p')
    
#view of category 
class CategoryList(ListView): 
    template_name= 'blog/category_list.html'
    paginate_by =2
   
    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.active(), slug=slug )
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category'] =category
        return context
#view of author
class AuthorList(ListView): 
    template_name= 'blog/author_list.html'
    paginate_by =2
   
    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author=get_object_or_404(User, username=username )
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['author'] =author
        return context
    
