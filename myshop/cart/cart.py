from decimal import Decimal
from django.conf import settings
from shop.models import Product
class Cart:
 def __init__(self,request):
        
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
     cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart
    print(f'cart sessionID {request.session.session_key}')
    print(f'cart sessionData : {cart}')

 def add(self,product,quantity=1,override_quantity=False):
            """
            add product to the cart or update its quantity 
            """
            product_id = str(product.id)
            if product_id not in self.cart:
               self.cart[product_id] = {'quantity': 0,
                              'price': str(product.price)}
            if override_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
             self.cart[product_id]['quantity'] += quantity
            self.save()
            print(self.cart)
 def save(self):
            self.session.modified = True 
            print("session modified")
 def remove(self,product):
             """
             remove product from the cart
             """
             product_id = str(product.id)
             if product_id in self.cart:
                 del self.cart[product_id]
                 self.save()
 def getTotalPrice(self):  
  return sum(Decimal(item['price'])* item['quantity'] for item in self.cart.values())
         

 def __iter__(self):
   """
   Iterate over the items in the cart and get the products
 from the database.
   """
   product_ids = self.cart.keys()
 # get the product objects and add them to the cart
   products = Product.objects.filter(id__in=product_ids)
   cart = self.cart.copy()
   for product in products:
    cart[str(product.id)]['product'] = product
    print(f'this is the cart.values from iter : {cart.values}')
   for item in cart.values():
    item['price'] = Decimal(item['price'])
    item['total_price'] = item['price'] * item['quantity']
    yield item
def __len__(self):
    """
            count all items in the cart
    """
    return sum(item['quantity'] for item in self.cart.values())

def clear(self):
            # remove cart from session
            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True
