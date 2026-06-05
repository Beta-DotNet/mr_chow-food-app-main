from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Cart, CartItem, Order
from django.db.models import Q

def _get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart

def home(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    cart = _get_or_create_cart(request)
    cart_items_count = sum(item.quantity for item in cart.items.all())

    return render(request, 'store/home.html', {
        'products': products,
        'query': query,
        'cart_items_count': cart_items_count
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_or_create_cart(request)
    cart_items_count = sum(item.quantity for item in cart.items.all())
    return render(request, 'store/product_detail.html', {
        'product': product,
        'cart_items_count': cart_items_count
    })

def cart_detail(request):
    cart = _get_or_create_cart(request)
    items = cart.items.all()
    total_price = sum(item.total_price for item in items)
    cart_items_count = sum(item.quantity for item in items)
    return render(request, 'store/cart_detail.html', {
        'cart': cart,
        'items': items,
        'total_price': total_price,
        'cart_items_count': cart_items_count
    })

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = _get_or_create_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, f"{product.name} added to cart.")
    return redirect('cart_detail')

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart = _get_or_create_cart(request)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('cart_detail')

def checkout(request):
    if request.method == 'POST':
        cart = _get_or_create_cart(request)
        items = cart.items.all()
        if not items:
            messages.error(request, "Your cart is empty.")
            return redirect('cart_detail')
        
        total_price = sum(item.total_price for item in items)
        order = Order.objects.create(total_price=total_price)
        cart.delete() # Clear the cart
        messages.success(request, f"Order #{order.id} placed successfully! Total: ${total_price}")
        return redirect('home')
    return redirect('cart_detail')
