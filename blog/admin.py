from django.contrib import admin
from .models import Article


#class for manage Article model in panel admin
class Articleadmin(admin.ModelAdmin):
    list_display =['status' , 'title' ]
    list_filter =('status',)
    search_fields =['title','descriptoin']
    prepopulated_fields = {'slug':('title',)}
    ordering =['status']

# Register your models here.
admin.site.register(Article,Articleadmin)