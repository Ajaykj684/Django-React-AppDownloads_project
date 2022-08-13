from django.urls import path
from . import views


urlpatterns = [

    path('',views.Myadmin.as_view(),name="myadmin"),
    path('adminlogin/',views.AdminLogin.as_view(),name="adminlogin" ),

    path('addapp/',views.AddApp.as_view(),name="addapp" ),
    path('deleteapp/<int:id>/',views.DeleteApp.as_view(),name="deleteapp" ),




]