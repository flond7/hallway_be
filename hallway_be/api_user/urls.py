from django.urls import path
from . import views

urlpatterns = [
  #path('login', views.index, name="login"),
  path('user_overview', views.user_overview, name="user_overview"),
  path('user_create', views.user_create, name="user_create"),
  path('user_ask', views.user_ask, name="user_ask"),
  path('user_edit/<str:pk>', views.user_edit, name="user_edit"),
  #url sotto creato per test di doppia pagina create - edit
  path('user_update/<str:pk>', views.user_update, name="user_update"),
  #path('user_add', views.user_add, name='user_add'),
  path('index', views.index, name="index"),
  path('login', views.login, name="login"),
  path('info', views.info, name="info"),
  path('profile/<str:pk>', views.profile, name="profile"),
  path('adweb', views.adweb, name="adweb"),
  path('iteratti', views.iteratti, name="iteratti"),
  path('sdi', views.sdi, name="sdi"),

  # BE API
  path('user_list', views.user_list, name="user_list"),
  path('office_list', views.office_list, name="office_list"),


  
  path('pauser_list_peg', views.pauser_list, name="pauser_list_peg"),
  path('pauser_po_list_peg', views.pauser_po_list, name="pauser_po_list_peg"),
  path('user_constants_list', views.user_constants_list, name="user_constants_list"),
  path('paoffice_list', views.paoffice_list, name="paoffice_list"),
  path('paoffice_and_po_list', views.paoffice_and_po_list, name="paoffice_and_po_list"),
  
  path('user_pacredential', views.user_pacredential, name="user_pacredential"),
  path('user_list_pacredential', views.user_list_pacredential, name="user_list_pacredential"),
 ] 