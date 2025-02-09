from django.urls import path,include

from man import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'review_for_product',views.review_viewset),
router.register(r'All_Review',views.ViewproductApiview)


urlpatterns = [
    path('', include(router.urls)),
    path("geans/",views.geans_list_post.as_view(),name='geans_list_post'),
    
    path("geans/<int:pk>/",views.details_geans_or_put_delete.as_view(),name='geans_list_post'),
    
    path("size_of_geans/",views.SizeOfGeansView.as_view(),name='size'),
    path("geans_brand/",views.BrandGeansView.as_view(),name='brand_geans'),
    path("geans_cetagory/",views.CetagoryGeansView.as_view(),name='cetagory'),
    
    
    path("brandShirt/",views.BrandShirtView.as_view(),name='brandShirt'),
    path("cetagoryshirt/",views.ShirtCetagoryView.as_view(),name='shirt-cetagory'),
    path('shirt/',views.ShirtListView.as_view(),name='shirt'),
    path('reviewForget/',views.ReviewForGetview.as_view(),name='sadf'),
    path('favourites/',views.FavView.as_view(),name='adsfds'),
    path('shirtDetails/<int:pk>/',views.ShirtDetailsView.as_view(),name='asdfsaffsdfds'),
    
    
    path('deleteRecentView/<int:pk>/',views.RecentViewDeleteApiview.as_view()),
    path('WatchCetagory/',views.WatchCetagoryView.as_view(),name='watchCetagory'),
    path('WatchBrand/',views.BrandWatchView.as_view(),name='brandWatch'),
    path('warenty/',views.WarentyView.as_view(),name='warenty'),
    path("diyal/",views.DiyalSizeview.as_view()),
    path('strapMetarail/',views.StrapMetarailview.as_view()),
    path('watch/',views.WatchProductView.as_view()),
    path('watchDetails/<int:pk>/',views.WatchDetailsView.as_view()),
    
    
    path('jackets/',views.ManJacketView.as_view()),
    path('brandjacket/',views.BrandJacketView.as_view()),
    path("typeofjacket/",views.TypeOfJacketView.as_view()),
    path('jacketwarrenty/',views.JacksWarrentyView.as_view()),
    path('jackdetails/<int:pk>/',views.JackDetailsView.as_view())
    ]
