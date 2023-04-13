import random

from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductReview
from apps.cart.cart import Cart

# Create your views here.


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))
    if len(related_products) >= 6:
        related_products = random.sample(related_products, 6)
     # Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', slug=slug)


    imagesstring = "{'image': '%s'}," % (product.image.url)

    for image in product.images.all():
        imagesstring = imagesstring + ("{'image': '%s'}," % (image.image.url))

    cart = Cart(request)    

    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False     

    context = {
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products,
    }

    return render(request, 'core/product.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    product = Product.objects.all()

    context = {
        'category':category,
        'product':product
    }

    return render(request, 'core/category.html', context)