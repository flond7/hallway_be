from django.urls import path
from . import views

urlpatterns = [ 
  path('get_csrf_token', views.get_csrf_token, name="get_csrf_token"),
  path('user_log', views.user_log, name="user_log"),
  path('get_user_profiles_auth/<int:pk>', views.get_user_profiles_auth, name="get_user_profiles_auth"),
  #path('user_log', views.user_log, name="user_log"),
 ] 