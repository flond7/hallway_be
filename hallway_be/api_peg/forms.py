from django import forms
from django.forms import ModelForm
from .models import goalPeg
 
 
# creating a form
class goalPegForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = goalPeg
        fields = '__all__'

       # https://www.webforefront.com/django/formtemplatelayout.html