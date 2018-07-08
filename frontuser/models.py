from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User



 
 
class Product(models.Model):
    MAIN_MENU = (
        ('mn', 'Men'),
        ('wm', 'Women'),
        ('ac', 'Accessories'),
        ('sh','Shoes'),
        ('kd','Kids'),
    )
    main_menu = models.CharField(
        max_length=2,
        choices=MAIN_MENU,
    )
   
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    modal= models.TextField(blank=True)

 
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
 
    def __str__(self):
        return self.name





class Cart(models.Model):
    profile = models.ForeignKey(User,on_delete='CASCADE')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete='CASCADE')
    quantity=models.IntegerField()
    size=models.CharField(max_length=7, db_index=True)
    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)
    
    class Meta:
        unique_together=('product','profile')

class Wishlist(models.Model):
    profile = models.ForeignKey(User, null=True,  on_delete='CASCADE')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(Product,null=True,on_delete='CASCADE')
    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)

    
    class Meta:
        unique_together=('product','profile')
