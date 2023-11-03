from django.urls import path
from . import views

urlpatterns = [
  path('goal_new', views.goal_create, name="goal_new"), 
  path('goals_new', views.create_multiple_goals, name='goals_new'),
 ] 