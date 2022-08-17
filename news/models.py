from django.db import models

# Create your models here.
from django.urls import reverse


class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    #author =
    photo = models.ImageField(default='book.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150,db_index=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category',kwargs={ 'category_id':self.pk })


