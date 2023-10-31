from django import forms
from django.forms import ModelForm
from .models import obbiettivoPeg
 
 
# creating a form
class obbiettivoPegForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = obbiettivoPeg
        fields = '__all__'

       # https://www.webforefront.com/django/formtemplatelayout.html