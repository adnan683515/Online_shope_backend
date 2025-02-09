from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    
    path('Football/',views.football_view.as_view(),name='football'),
    path('allfootball/',views.AllFootballsJust.as_view()),
    path("team/",views.TeamView.as_view(),name='team'),
    path("version/",views.VersionView.as_view(),name='adsfas'),
    path('CricketBrand/',views.CricketBrandView.as_view(),name='brand'),
    path("mainmetarial/",views.MainMetarailView.as_view(),name='asdfsadfdsfsdf'),
    path("SportsDetails/<int:pk>/",views.SportSdetailis.as_view(),name='sportsdetails'),
    path('Batsize/',views.BatSizeView.as_view(),name='batsize'),
    path('alljursery/',views.AllJurseyView.as_view())
    ]
