
from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'powder_all', views.powder_viewset),
router.register(r'review_powder',views.powder_review_viewset)


urlpatterns = [
    path('', include(router.urls)),
    path('powder/',views.powder_views.as_view(),name='powder'),
    path("powder/<int:pk>/",views.details_powder_or_put_delete.as_view(),name='powder_single')

    ]
