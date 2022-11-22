import json
import stripe

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest

from apps.cart.cart import Cart

from apps.order.utils import checkout

from .models import  Product
from apps.core.models import Coupon
from apps.order.models import Order, OrderItem

from .utilities import decrement_product_quantity, send_order_confirmation

def create_checkout_session(request):
    data = json.loads(request.body)

    # Coupon 

    coupon_code = data['coupon_code']
    coupon_value = 0

    if coupon_code != '':
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            coupon_value = coupon.value
            coupon.use()

    #

    cart = Cart(request)
    items = []
    
    for item in cart:
        product = item['product']

        price = int(product.price * 100)

        if coupon_value > 0:
            price = int(price * (int(coupon_value) / 100))

        obj = {
            'price_data': {
                'currency': 'nok',
                'product_data': {
                    'name': product.name
                },
                'unit_amount': price
            },
            'quantity': item['quantity']
        }

        items.append(obj)

    gateway = data['gateway']
    session = ''
    order_id = ''
    payment_intent = ''
    
    if gateway == 'stripe':
        stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='https://stellcare.com/handlekurv/order-success/',
            cancel_url='https://stellcare.com/handlekurv/'
        )
        payment_intent = session.payment_intent

    #
    # Create order

    orderid = checkout(request, data['first_name'], data['last_name'], data['email'], data['address'], data['zipcode'])

    total_price = 0.00

    for item in cart:
        product = item['product']
        total_price = total_price + (float(product.price) * int(item['quantity']))

    if coupon_value > 0:
        total_price = total_price * (coupon_value / 100)
        
    # PayPal

    if gateway == 'paypal':
        order_id = data['order_id']
        environment = SandboxEnvironment(client_id=settings.PAYPAL_API_KEY_PUBLISHABLE, client_secret=settings.PAYPAL_API_KEY_HIDDEN)
        client = PayPalHttpClient(environment)

        request = OrdersCaptureRequest(order_id)
        response = client.execute(request)

        order = Order.objects.get(pk=orderid)
        order.paid_amount = total_price
        order.used_coupon = coupon_code

        if response.result.status == 'COMPLETED':
            order.paid = True
            order.payment_intent = order_id
            order.save()

            decrement_product_quantity(order)
            send_order_confirmation(order)
        else:
            order.paid = False
            order.save()
    else:
        order = Order.objects.get(pk=orderid)
        if gateway == 'razorpay':
            order.payment_intent = payment_intent['id']
        else:
            order.payment_intent = payment_intent
        order.paid_amount = total_price
        order.used_coupon = coupon_code
        order.save()

    #

    return JsonResponse({'session': session, 'order': payment_intent})

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'succes': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)

def api_add_to_cart_bundle(request):
    data = json.loads(request.body)
    jsonresponse = {'succes': True}
    bundle_id = data['bundle_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    bundle = get_object_or_404(Bundle, pk=bundle_id)

    if not update:
        cart.add_bundle(bundle=bundle, quantity=1, update_quantity=False)
    else:
        cart.add_bundle(bundle=bundle, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)        


def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'succes': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)  


def api_can_use(request):
    json_response = {}

    coupon_code = request.GET.get('coupon_code', '')

    try:
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            json_response = {'amount': coupon.value}
        else:
            json_response = {'amount': 0}
    except Exception:
        json_response = {'amount': 0}

    return JsonResponse(json_response)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)