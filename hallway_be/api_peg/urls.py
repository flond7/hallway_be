from django.urls import path
from . import views

urlpatterns = [
  path('goal_new', views.goal_create, name="goal_new"), 
  path('create_multiple_goals', views.create_multiple_goals, name='create_multiple_goals'),
  path('delete_multiple_goals', views.delete_multiple_goals, name='delete_multiple_goals'),
  path('update_multiple_goals', views.update_multiple_goals, name='update_multiple_goals'),
  path('get_person_results', views.get_person_results, name='get_person_results'),
  path('get_po_results', views.get_po_results, name='get_po_results'),
  path('get_office_results', views.get_office_results, name='get_office_results'),
  path('get_goals_numbers', views.get_goals_numbers, name='get_goals_numbers'),
  path('check_existing_goals', views.check_existing_goals, name='check_existing_goals'),
  path('get_average_weight', views.get_average_weight, name='get_average_weight'),
  path('get_person_min_results', views.get_person_min_results, name='get_person_min_results'),
 ] 