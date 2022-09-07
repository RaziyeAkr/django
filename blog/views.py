import re
from django.core.paginator import Paginator
from django.views.generic import ListView ,DetailView
from django.shortcuts import render ,get_object_or_404
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
'''def category(request , slug, page=1):

    category=get_object_or_404(Category, slug=slug ,status=True)
    articles_list=category.articles.published()
    paginator= Paginator(articles_list,2)
    articles=paginator.get_page(page)
    
    context = {
        'category' : category,
        "articles": articles
    }
    return render(request , "blog/category.html" , context)'''
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

    
