from . import views
from django.urls import path


urlpatterns = [

    path('sslcomarce/',views.SSLCOMARCEAPIVIEW.as_view()),
    path('success/', views.SSLCommerzSuccessView.as_view(), name='payment_success'),
    path('fail/', views.SSLCommerzFailView.as_view(), name='payment_fail'),
    path('cancel/', views.SSLCommerzCancelView.as_view(), name='payment_cancel'),

    ]
