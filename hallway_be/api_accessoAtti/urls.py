from django.urls import path
from . import views

urlpatterns = [
  #path('login', views.index, name="login"),
  path('access_new', views.access_create, name="access_new"), 
  path('access_delete/<int:pk>', views.access_delete, name="access_delete"), 
  path('access_list', views.access_list_all, name="access_list"), 
#path('access_record', views.access_create, name="access_record"), 
 ] 