from django.urls import path
from . import views




from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('',views.Home.as_view(),name="home"),
    path('login/',views.Login.as_view(),name="login"),
    path('register/',views.Register.as_view(),name="register"),


    path('appdownload/<int:id>/<int:userId>/',views.AppDownload.as_view(),name="appdownload" ),
    path('taskCompleted/<int:id>/',views.TaskCompleted.as_view(),name="taskCompleted" ),
    path('taskDetails/<int:id>/',views.TaskDetails.as_view(),name="taskDetails" ),


    path('userDetails/<int:id>/',views.UserDetails.as_view(),name="appdownload" ),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]
