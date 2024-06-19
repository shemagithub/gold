from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from . forms import CustomerRegistrationForm, CustomerProfileForm, ContactForm

from .models import Products, Cart, Customer, Blog, Testimonial, Subscribe
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
from .forms import ProductSearchForm

# Create your views here.
def home(request):
    testimony = Testimonial.objects.all()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))      
    return render(request, 'app/home.html',locals())

def shop(request):
    products = Products.objects.all()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, "app/shop.html" ,locals())

def blog(request):
    blog = Blog.objects.all()
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    return render(request, "app/blog.html" , locals())

def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Cart.objects.filter(user=request.user))

    return render(request ,"app/about.html",locals())

def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', locals())
  
def sub(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            
    else:
        form = ContactForm()
    return render(request, 'app/base.html', {'form': form})
  

def cash(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Cart.objects.filter(user=request.user))

    return render(request ,"app/cash.html", locals())

def customer_list(request):
    customers = Customer.objects.all()  # Fetch all customers from the database
    return render(request, 'app/chackout.html', {'customers': customers})

def product_search(request):
    form = ProductSearchForm()
    products = []
    if 'query' in request.GET:
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Products.objects.filter(title__icontains=query)
    
    return render(request, 'app/product_search.html', {'form': form, 'products': products})

def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'app/shop-detail.html', {'product': product})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Conglutaration! User Register SuccesFully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, "app/customerregistration.html",locals())
    


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Cart.objects.filter(user=request.user))

        return render(request,"app/updateAddress.html",locals())
        
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Update Succesfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")
    
class checkout(View):
    def get(self,request):
        user = request.user
        add=Customer.objects.filter(user=user)
        cart_items= Cart.objects.filter(user=user)
        customers = Customer.objects.all() 
        
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = + value
        totalamount = famount + 1000               
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        return render(request,"app/chackout.html",locals())



class ProfileView(View):
     def get(self,request):
         form = CustomerProfileForm()
         return render(request, "app/profile.html",locals())
     def post(self,request):
         form = CustomerProfileForm(request.POST)
         totalitem = 0
         wishitem = 0
         if form.is_valid():
             user = request.user
             name = form.cleaned_data['name']
             locality = form.cleaned_data['locality']
             city = form.cleaned_data['city']
            
             state = form.cleaned_data['state']
             zipcode = form.cleaned_data['zipcode']

             reg = Customer(user=user, name=name, locality=locality,  city=city, state=state, zipcode=zipcode)
             reg.save()
             messages.success(request,"Congratuulation profile save succesfully")
         else:
             messages.warning(request,"Invalid Input Data")

         if request.user.is_authenticated:
             totalitem = len(Cart.objects.filter(user=request.user))
             wishitem = len(Cart.objects.filter(user=request.user))
             
         return render(request, "app/profile.html",locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Cart.objects.filter(user=request.user))

    return render(request, "app/address.html",locals())


def add_to_cart(request):
    user = request.user
    product_id=request.GET.get('prod_id')
    product= Products.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Cart.objects.filter(user=request.user))

    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 1000
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Cart.objects.filter(user=request.user))

    return render(request,"app/cart.html",locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user)).first()
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(prod_id)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 1000
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 1000
        #print(prod_id)
        data ={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 1000
        #print(prod_id)
        data ={
            
            'amount':amount,
            'totalamount':totalamount

        }
        return JsonResponse(data)
    