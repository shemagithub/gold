from django.contrib import admin
from .models import Products, Customer, Cart, ContactForm, Blog, Testimonial, Subscribe

#
# Register your models here.
@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(ContactForm)
class SubscribeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

@admin.register(Subscribe)
class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

@admin.register(Blog)
class BlogFormModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','name','blog_image','date']


@admin.register(Testimonial)
class BlogFormModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','testimony','name','profile_image']
