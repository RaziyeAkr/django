from django.db import models

# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
    )
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=50,unique=True)
    descriptoin=models.TextField()
    thumnail=models.ImageField(upload_to='images')
    status=models.CharField(max_length=1,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
