from django.db import models
from django.contrib.auth.models import User
from product_app.models import Product
# Create your models here.
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User







class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return f"Cart for {self.user.username}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart,  related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return f"Cart Items-> x {self.product.product_title}"


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ], default='Pending')
    zila = models.CharField(max_length=100,null=True,blank=True)
    upzila = models.CharField(max_length=200,null=True,blank=True)
    shipping_address = models.TextField()
    quantity = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    oderdate = models.DateField(auto_now_add=True,blank=True,null=True)
    tranjection_id = models.CharField(max_length=100,null=True,blank=True)

    
    def __str__(self):
        return f"Order #{self.id} for {self.user.username}"
