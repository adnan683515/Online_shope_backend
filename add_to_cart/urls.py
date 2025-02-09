
from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('cart/',views.CartView.as_view()),
    path('cartItems/',views.CartItemsView.as_view()),
    path('order/',views.orderView.as_view()),
    path('updatecart/<int:pk>/',views.CartItemsUpdate.as_view()),
    path('user/<int:pk>/',views.user_details.as_view()),
    path('oderlist/',views.OrderListapiView.as_view()),
    path('oderPut/<int:pk>/',views.OderPut.as_view()),
    path('oder_filter/',views.FilterOderlist.as_view())
    ]


















  