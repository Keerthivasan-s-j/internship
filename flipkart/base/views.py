from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User #to use the User Table
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages #used to display messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #importing the login required decorator
from django.db.models import Q
from .models import Feedback,Product,Cart,CartItem

# Landing Page
@login_required(login_url='login')
def landingpage(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        products = None
        if query:
            products = Product.objects.filter(prod_name__icontains=query)
        else:
            products = Product.objects.all()
            query = 'Products'
        context = {'products': products, 'query': query}
        return render(request, 'index.html', context=context)
    
    # Handle GET requests (no search query)
    products = Product.objects.all()
    count = products.count()
    context = {'products': products, 'query': 'Products', 'no_items' : count}
    return render(request, 'index.html', context=context)

# User Login
def user_login(request):
    if request.method == 'POST':
        uname_or_email = request.POST.get('uname_or_email')
        password = request.POST.get('pwd')
        error_message = 'kl'
        if '@' in uname_or_email:
            user = authenticate(email = uname_or_email, password = password)
        else:
            user = authenticate(username = uname_or_email, password = password)
        
        if user is not None:
            login(request, user) #this login function is from the django.contrib.auth
            return redirect(reverse('landingpage'))
        else:
            error_message  = 'Invalid credentials. Please try again.'
            return render(request, 'auth/login.html', context={'error_message' : error_message})
    return render(request, 'auth/login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect(reverse('login'))

# Sign Up
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
    
        if password == con_password:
            if User.objects.filter(username = username).exists(): #checks for the existance of the user
                return redirect(reverse('login'))
            else:
                User.objects.create_user(username=username,email=email,password=password, first_name = fname, last_name = lname)
                return redirect(reverse('login'))
        else:
            return render(request, 'auth/signup.html')
            
    return render(request, 'auth/signup.html')

# Add Feedback
@login_required(login_url='login')
def add_feedback(request):
    if request.method == 'POST':
        fname = request.user.first_name
        lname = request.user.last_name
        email = request.user.email
        ratings = request.POST.get('exp')
        message = request.POST.get('message')
        # Saving the product instance
        feedback = Feedback.objects.create(
            fname = fname,
            lname = lname,
            email = email,
            ratings = int(ratings),
            message = message
        )
        return redirect(reverse('landingpage'))
    return render(request, 'feedback/feedback.html')

def aboutus(request):
    return render(request, 'about.html')

# Cart
@login_required(login_url='login')
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        grand_total = sum(item.total_price() for item in cart_items)
        context = {'cart_items': cart_items, 'grand_total': grand_total}
    except Cart.DoesNotExist:
        cart_items = []
        grand_total = 0
        context = {'cart_items': cart_items, 'grand_total': grand_total}
    
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Increment's The Quantity when the product is already exist the changes need to be saved explicitly
    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(reverse('cart'))

@login_required(login_url='login')
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect(reverse('cart'))

# Add Product
@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        fname = request.user.first_name #fetches the first name of the current logined user
        lname = request.user.last_name
        email = request.user.email
        # phone = request.POST.get('phone')
        # address = request.POST.get('address')
        prod_name = request.POST.get('prod_name')
        prod_price = request.POST.get('prod_price')
        prod_discount = request.POST.get('prod_discount')
        category = request.POST.get('category')
        prod_details = request.POST.get('prod_details')
        prod_img = request.FILES.get('prod_img')

        data = Product.objects.create(
            seller_name = fname + " " + lname,
            seller_email = email,
            # seller_phone = phone,
            # seller_address = address,
            prod_name = prod_name,
            prod_image = prod_img,
            prod_details = prod_details,
            prod_price = prod_price,
            prod_category = int(category),
            discount = prod_discount if prod_discount else 0
        )
        return redirect(reverse('landingpage'))
    return render(request, 'addproduct.html')

# Buy Product View
@login_required(login_url='login')
def buy(request):
    return render(request, 'success.html')

# Buy all the product from the cart
@login_required(login_url='login')
def buy_from_cart(request):
    CartItem.objects.filter(cart = request.user.cart).delete()
    return redirect(reverse('buy'))

# Create your views here.
