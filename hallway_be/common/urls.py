from django.urls import path
from . import views

urlpatterns = [ 
  path('get_csrf_token', views.get_csrf_token, name="get_csrf_token"),
  path('user_log', views.user_log, name="user_log"),
  #path('access_list', views.access_list_all, name="access_list"), 
 ] 