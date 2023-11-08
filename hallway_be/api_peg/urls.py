from django.urls import path
from . import views

urlpatterns = [
  path('goal_new', views.goal_create, name="goal_new"), 
  path('goals_new', views.create_multiple_goals, name='goals_new'),
  path('get_person_results', views.get_person_results, name='get_person_results'),
  path('get_goals_numbers', views.get_goals_numbers, name='get_goals_numbers'),
  #path('get_person_results', views.get_person_results, name='get_person_results'),
 ] 