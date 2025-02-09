
from . import views
from django.urls import path


urlpatterns = [
    # path("product_list/",views.saree_list_api_view.as_view(),name='saree_list'),
    path("saree_review/",views.saree_review_list_api_view.as_view(),name='saree_review'),
    path('saree/',views.saree_api_view.as_view(),name='saree_post'),
    path('saree/<str:product_title>/',views.saree_api_view.as_view(),name='saree_search'),
    
    path("saree_details/<int:pk>/",views.details_saree_or_put_delete.as_view(),name='single_saree'),
    path("view_saree/",views.view_saree.as_view(),name='view_saree'),
    path("saree_cetagory/",views.saree_cetagory_api_view.as_view(),name='saree_cetagory'),
    path("colour/",views.colour_api_view.as_view(),name='colour'),
    path("range_of_price/",views.range_of_price_view.as_view(),name='price'),
    path('brand_saree/',views.brand_saree_view.as_view(),name='brand-saree')
    
    ]
