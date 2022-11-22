from django.conf import settings
from django.http.response import Http404

from apps.store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()        
        product_clean_ids = []

        bundle_ids = self.cart.keys()        
        bundle_clean_ids = []

        for p in product_ids:
            product_clean_ids.append(p)
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)    

        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item
        
        
        # try:
        #     for b in bundle_ids:
        #         bundle_clean_ids.append(p)
        #         self.cart[str(b)]['bundle'] = Bundle.objects.get(pk=b)             

        #     for bundleC in self.cart.values():
        #         bundleC['total_price'] = float(bundleC['price']) * int(bundleC['quantity'])

        #         yield bundleC
        # except Bundle.DoesNotExist:
        #     return None   
       
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        print('Product_id:', product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1


        self.save()

    def add_bundle(self, bundle, quantity=1, update_quantity=False):
        bundle_id = str(bundle.id)
        price = bundle.price

        print('Bundle_id:', bundle_id)

        if bundle_id not in self.cart:
            self.cart[bundle_id] = {'quantity': 0, 'price': price, 'id': bundle_id}
        
        if update_quantity:
            self.cart[bundle_id]['quantity'] = quantity
        else:
            self.cart[bundle_id]['quantity'] = self.cart[bundle_id]['quantity'] + 1


        self.save()    
    
    def has_product(self, product_id):
        if str(product_id) in self.cart:
            return True
        else:
            return False       

    def has_bundle(self, bundle_id):
        if str(bundle_id) in self.cart:
            return True
        else:
            return False        
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_length(self):
        return sum(int(item['quantity']) for item in self.cart.values())
    
    def get_total_cost(self):
        return sum(float(item['total_price']) for item in self)



