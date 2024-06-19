from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100)   
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

STATE_CHOICES=(
    ('KIGALI','RWANDA'),
    ('MUSANZE','RWANDA'),
    ('RUBAVU','RWANDA'),
    ('KAYONZA','RWANDA'),
    ('GASABO','RWANDA'),
    ('MUHANGA','RWANDA'),
    ('NYAMASHEKE','RWANDA'),
    ('GISAARA','RWANDA'),
    ('RUSIZI','RWANDA'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price





class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100)   
    description = models.TextField()
    name = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='product')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=100)   
    testimony = models.TextField()
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='product')   
    def __str__(self):
        return self.title
    

