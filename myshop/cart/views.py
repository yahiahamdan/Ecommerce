from django.shortcuts import render,redirect,get_object_or_404
from .forms import CartAddPrdouctForm
# Create your views here.
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddPrdouctForm

@require_POST
def cart_add(request,product_id):
    print("cart add view called")
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddPrdouctForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      print("form is valid")
      cart.add(product=product,
          quantity=cd['quantity'],
          override_quantity=cd['override'])
      return redirect('cart:cart_detail')
    else:
        print("form is invalid",form.errors)
        return redirect('cart:cart_detail')


def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart=Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddPrdouctForm(initial={
         'quantity': item['quantity'],
 'override': True})

    totalPrice= cart.getTotalPrice()
    return render(request,'cart/detail.html',{'cart':cart,'totalPrice':totalPrice})
