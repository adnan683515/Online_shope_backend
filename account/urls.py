from . import views
from django.urls import path


urlpatterns = [

    path('register/',views.register_view.as_view(),name='register'),
    path('active/<uidb64>/<token>/',views.activate),
    path('login/',views.log_in_view.as_view(),name='login'),
    path('logout/',views.logoutView.as_view(),name='login'),
    path('user/<int:pk>/',views.userDetails.as_view(),name='user'),
    path('adminstaff/<int:pk>/',views.adminSaff.as_view()),
    path('pass/',views.passwordview.as_view())
    ]
