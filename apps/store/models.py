from itertools import product
from django.db import models
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(blank=False, default='none')
    is_home_page = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % (self.slug)      


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(max_length=300, default=0)
    discount_price = models.FloatField(max_length=300, default=0)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True, max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=False)
    num_available = models.IntegerField(default=1)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def admin_photo(self):
            return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = 'image'
    admin_photo.allow_tags = True


    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)    

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category, self.slug)    

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


        

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def admin_photo(self):
            return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = 'image'
    admin_photo.allow_tags = True
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)

