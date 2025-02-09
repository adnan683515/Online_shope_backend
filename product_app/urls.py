
from . import views
from django.urls import path






urlpatterns = [

    path('delivery/',views.DeliveryView.as_view(),name='delivery'),
    path('viewproduct/',views.viewModelObject.as_view()),
    path('viewDelete/<int:pk>/',views.ViewMOdelapiview.as_view()),
    path('brandpost/',views.BrandPost.as_view()),
    path('cetagorypost/',views.CetagoryPost.as_view()),
    path('courntrypost/',views.CountryPost.as_view()),
    path('colourpost/',views.ColourPost.as_view()),
    path('sizepost/',views.SizePOst.as_view()),
    path('deletecolourput/<int:pk>/',views.DeletePUtColour.as_view()),
    path('brandPutDelte/<int:pk>/',views.BrandDeletePUT.as_view()),
    path('countryPutDelet/<int:pk>/',views.CountryPUTDelete.as_view()),
    path('cetagoryputdelete/<int:pk>/',views.CetagoryPUTDelete.as_view()),
    path('allteam/',views.AllTeam.as_view()),
    path('teamputdelte/<int:pk>/',views.TeamNameDeleteAndPut.as_view()),
    path('mainmetarials/',views.MainMetarialsApiView.as_view()),
    path('editdeletemeta/<int:pk>/',views.EditMetaDelete.as_view()),
    path('versionpost/',views.VersionPost.as_view()),
    path('versionputdelete/<int:pk>/',views.VersionPutDelete.as_view()),
    path('TypeOfjaceketPost/',views.TypeOfjaceketPost.as_view()),
    path('JacketPutDelete/<int:pk>/',views.JacketPutDelete.as_view()),
    path('RangePriceDeletePut/<int:pk>/',views.RangePriceDeletePut.as_view()),
    path('MoveMentWatchPostGEt/',views.MoveMentWatchApi.as_view()),
    path('MoveMentPutDelApivew/<int:pk>/',views.MoveMentPutDelApivew.as_view()),
    path('SizeApiView/',views.SizeApiView.as_view()),
    path('productpost/',views.ProductPostApiViw.as_view()),
    path('sizeupdate/<int:pk>/',views.SizeUpdate.as_view()),
    path('WarrentyApiView/',views.WarrentyApiView.as_view()),
    path('WarrentyCrudApiview/<int:pk>/',views.WarrentyCrudApiview.as_view())
    ]
