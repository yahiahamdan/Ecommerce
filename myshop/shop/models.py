from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
        indexes=[models.Index(fields=['slug'])]
    def _str_(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
    

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("show:product_detail",args=[self.id,self.slug])
    

    class Meta:
        ordering=('name',)
        indexes=[
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),       
            models.Index(fields=['-created'])
             ]
    def _str_(self):
        return self.name