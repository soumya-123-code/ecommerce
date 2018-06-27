from django.contrib import admin
from frontuser.models import Category,Product


from django.utils.datetime_safe import datetime

from frontuser.models import Product, Cart


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)




class EntryAdmin(admin.ModelAdmin):
    # Overide of the save model
    def save_model(self, request, obj, form, change):
        obj.cart.total += obj.quantity * obj.product.cost
        obj.cart.count += obj.quantity
        obj.cart.updated = datetime.now()
        obj.cart.save()
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Cart)
