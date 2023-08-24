from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# MY VARS
#from .constants import MY_CONST
#from .modelsConstants import *
from .models import accessoAtti
from .forms import accessoAttiForm
#from .serializers import UserListSerializer

# Create your views here.
def access_create(request):
    if request.method == "POST":
        cu = accessoAttiForm(request.POST)
        if cu.is_valid():
            cu.save()
            return "Record saved correctly"           
    return False

def access_list_all(request):
    if request.method == "GET":
        accessList = accessoAtti.objects.all()
        return accessList          
    