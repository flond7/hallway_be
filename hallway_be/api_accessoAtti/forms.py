from django import forms
from django.forms import ModelForm
from .models import accessoAtti
 
 
# creating a form
class accessoAttiForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = accessoAtti
        fields = '__all__'

       # https://www.webforefront.com/django/formtemplatelayout.html