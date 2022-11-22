from django.shortcuts import render
from django.conf import settings
from .cart import Cart

# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    productsstring = ''
    bundlesstring = ''

    for item in cart:
        product = item['product']
        p = "{'id': '%s', 'name': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'num_available': '%s'}," % (product.id, product.name, product.price, item['quantity'], item['total_price'], product.thumbnail.url, product.num_available)

        productsstring = productsstring + p
        
    # for bundleC in cart:    
    #     bundle = bundleC['bundle']
    #     b = "{'id': '%s', 'name': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (bundle.id, bundle.name, bundle.price, bundleC['quantity'], bundleC['total_price'])

    #     bundlesstring = bundlesstring + b
     

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
    else:
        first_name = last_name = email = ''     

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'pub_key_paypal': settings.PAYPAL_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(','),
        'bundlesstring': bundlesstring.rstrip(','),
        
    }
    
    return render(request, 'core/cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'core/success.html')

def checkout(request):
    return render(request, 'core/checkout.html')    