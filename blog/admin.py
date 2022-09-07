from unicodedata import category
from django.contrib import admin
from .models import Article , Category
#model 1
class Categoryadmin(admin.ModelAdmin):
    list_display =['position','status' , 'title' ,'slug','parent' ]
    list_filter =(['status'])
    search_fields =['title']
    prepopulated_fields = {'slug':('title',)}
    
    

# Register your models here.
admin.site.register(Category,Categoryadmin)
#model 2
#class for manage Article model in panel admin
class Articleadmin(admin.ModelAdmin):
    list_display =['status' , 'title' ,'Category_to_str']
    list_filter =('status',)
    search_fields =['title','descriptoin']
    prepopulated_fields = {'slug':('title',)}
    ordering =['status']
    def Category_to_str(self , obj):
        return ", ".join([category.title for category in obj.category_publish()])
    Category_to_str.short_description ="نوع دسته بندی"


# Register your models here.
admin.site.register(Article,Articleadmin)