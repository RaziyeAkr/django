from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100 ,verbose_name ="عنوان دسته بندی")
    slug=models.SlugField(max_length=50,unique=True, verbose_name="ادرس دسته بندی")
    status=models.BooleanField(verbose_name="ایا ذخیره شود؟")
    position =models.IntegerField(verbose_name="وضعیت")
    class Meta():
        verbose_name ="دسته بندی"
        verbose_name_plural ="دسته بندی ها"
        
    def __str__(self):
        return self.title

#Second
class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    title=models.CharField(max_length=100 ,verbose_name ="عنوان مقاله")
    slug=models.SlugField(max_length=50,unique=True, verbose_name="ادرس")
    category =models.ManyToManyField(Category,verbose_name="نوع دسته بندی")
    descriptoin=models.TextField(verbose_name="توضیحات مقاله")
    thumnail=models.ImageField(upload_to='images', verbose_name="عکس مقاله")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت مقاله")
    class Meta():
        verbose_name ="مقاله"
        verbose_name_plural ="مقالات"
    def __str__(self):
        return self.title
