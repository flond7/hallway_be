from django import forms
from django.forms import ModelForm
from .models import customUser, askUser
 
 
# creating a form
class customUserForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = customUser
        fields = '__all__'

        labels = {
            'name': '',
            'surname': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'rounded border-none w-100 create-form-input', 'placeholder': 'Nome'}),
            'surname': forms.TextInput(attrs={'class': 'create-form-input', 'placeholder': 'Cognome'})
        }

       # https://www.webforefront.com/django/formtemplatelayout.html


class askUserForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = askUser
        fields = '__all__'

        labels = {
            'name': '',
            'surname': '',
            'office': '',
            'lanOffice': '',
            'boxAppsRole': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'rounded border-none col-md-3 float-left me-3 create-form-input', 'placeholder': 'Nome'}),
            'surname': forms.TextInput(attrs={'class': 'rounded border-none col-md-3 float-left me-3 create-form-input', 'placeholder': 'Cognome'}),
            'office': forms.Select(attrs={'class': 'col-md-4 create-form-input'}),
            """ 'mailOffice': forms.BooleanField(), """
            'lanOffice': forms.CheckboxSelectMultiple(attrs={'class': 'col-md-6 create-form-input float-left'}),
            'lanRole': forms.Select(attrs={'class': 'col-md-6'}),
            'boxAppsRole': forms.Select(attrs={'class': 'col-md-2'}),
            'masterDataRole': forms.Select(attrs={'class': 'col-md-2'}),
            'websiteRole': forms.Select(attrs={'class': 'col-md-2'}),
            'ammTraspRole': forms.Select(attrs={'class': 'col-md-2'}),
            'crmRole': forms.Select(attrs={'class': 'col-md-2'}),
            'avcpRole': forms.Select(attrs={'class': 'col-md-2'}),
            'fvgPayRole': forms.Select(attrs={'class': 'col-md-2'}),
            'mepaRole': forms.Select(attrs={'class': 'col-md-2'}), 
            'agEntrRole': forms.Select(attrs={'class': 'col-md-2'}),
            'sueRole': forms.Select(attrs={'class': 'col-md-2'}),
            'suapRole': forms.Select(attrs={'class': 'col-md-2'}),
            'servScolRole': forms.Select(attrs={'class': 'col-md-2'}),
            'alboPretRole': forms.Select(attrs={'class': 'col-md-2'}),
            'ammTraspRole': forms.Select(attrs={'class': 'col-md-2'}),
            'note': forms.Textarea(attrs={'class': 'col-md-12 create-form-input'})
            
        }