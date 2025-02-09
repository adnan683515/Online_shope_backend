from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from add_to_cart.models import Order,CartItem
from sslcommerz_lib import SSLCOMMERZ 
from product_app.models import Product
# Create your views here.

import uuid
import time


from functools import wraps
from django.utils.decorators import decorator_from_middleware
from corsheaders.middleware import CorsMiddleware

def cors_allow_all(view_func):
    @wraps(view_func)
    def _wrapped_view(*args, **kwargs):
        response = decorator_from_middleware(CorsMiddleware)(view_func)(*args, **kwargs)
        # Allow all origins
        response["Access-Control-Allow-Origin"] = "*"
        return response

    return _wrapped_view

def generate_transaction_id():
    timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
    unique_id = uuid.uuid4().hex  # Random unique ID (UUID)
    transaction_id = f"{timestamp}-{unique_id}"
    return transaction_id



class SSLCOMARCEAPIVIEW(APIView):  
    
    @cors_allow_all
    def post(self,request,format=None):
        cart_item_id = self.request.query_params.get('oder_id')
        obj  = CartItem.objects.get(pk=cart_item_id)
        settings = { 'store_id': 'adnan676ea5e2eccdf', 'store_pass': 'adnan676ea5e2eccdf@ssl', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = obj.price
        post_body['currency'] = "BDT"
        post_body['tran_id'] = generate_transaction_id()
        post_body['success_url'] = f'http://127.0.0.1:8000/success/?user_id={request.user.id}&item_id={obj.id}'
        post_body['fail_url'] = ""
        post_body['cancel_url'] = "your cancel url"
        post_body['emi_option'] = 0
        post_body['cus_name'] = request.user.username
        post_body['cus_email'] = request.user.email
        post_body['cus_phone'] = "01700000000"
        post_body['cus_add1'] = "customer address"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"


        response = sslcz.createSession(post_body) # API response
        print(response.get("GatewayPageURL"))
        return redirect(response['GatewayPageURL'])
    # Need to redirect user to response['GatewayPageURL']

class SSLCommerzSuccessView(APIView):
    def post(self, request):
        User_id = self.request.query_params.get('user_id')
        item_id = self.request.query_params.get('item_id')
        obj = CartItem.objects.get(pk=item_id)
        product = Product.objects.get(pk=obj.product.id)
        product.quantity -= obj.quantity
        product.save()
        return redirect(f'http://127.0.0.1:5500/checkout.html?item_id={item_id}')

class SSLCommerzFailView(APIView):
    def post(self, request):
        # Handle failed payment
        return Response({"status": "fail", "data": request.data})

class SSLCommerzCancelView(APIView):
    def post(self, request):
        # Handle canceled payment
        return Response({"status": "cancel", "data": request.data})
    
        
        