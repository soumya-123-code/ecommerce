from django.db import models

class Category(models.Model):
    MAIN_MENU = (
        ('mt', 'Men-TShirt'),
        ('sh', 'Shoes'),
        ('mb', 'Mobile')
    )
    main_menu = models.CharField(
        max_length=2,
        choices=MAIN_MENU,
    )
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    def __str__(self):
        return self.name
 
 
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='tag', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
 
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
 
    def __str__(self):
        return self.name




#Category Model

#The category model consist of four fields:
  #  name – which has a maximum length of 150 characters

   # slug – which is a unique field, this help us in building canonical urls later.

  #  created_at – which tracks when category was created.

  #  updated_at – which tracks when category was updated.

#  Product Model

#The product model consist of ten fields:

 #   name – which has a maximum length of 100 characters.

  #  category – which is foreign-key pointing to our category model. A product belong to a category. In this field we have added on_delete argument which is the behavior to adopt when referenced object is deleted.

   # slug – which we will use for building seo friendly url.

   # description – which is used to describe a product.

 #   price – which used for holding price of a product. We are using DecimalField to avoid rounding off issues.

 #   image – used to hold image of a product.

   # available – this is boolean field used to show whether product is available or not.

  #  stock – this is positive integer to show number of stock of given product.

  #  created_at – which tracks when product was created.

   # updated_at – which tracks when product was updated.


