from django.contrib import admin

# Register your models here.
from .models import Item, Coupon, Customer

admin.site.register(Item)
admin.site.register(Coupon)
admin.site.register(Customer)