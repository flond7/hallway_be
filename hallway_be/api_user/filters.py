import django_filters
from .models import customUser

""" 
field_name: The name of the model field to filter on. 
lookup_expr: the WHERE clause 
"""

class customUserFilter(django_filters.FilterSet):
  #name_filter = django_filters.CharFilter(lookup_expr='name')
  #name = django_filters.CharFilter(lookup_expr='iexact')

  class Meta:
    model = customUser
    fields = {'name': ['exact'], 'surname': ['exact'], 'office': ['exact'], 'active':['exact'], 'employed': ['exact']}
