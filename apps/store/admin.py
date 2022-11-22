
# Register your models here.

import datetime

from django.contrib import admin
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from .models import Product, Category, ProductImage, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ['admin_photo', 'name', 'parent', 'category', 'price', 'num_available', 'is_popular', 'is_sale', 'is_featured']

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)  


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['admin_photo', 'product']
admin.site.register(ProductImage, ProductImageAdmin)  

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'stars', 'date_added']
admin.site.register(ProductReview, ProductReviewAdmin)   
 
