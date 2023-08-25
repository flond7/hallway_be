from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

#CORS
from django.views.decorators.csrf import csrf_exempt

# MY VARS
#from .constants import MY_CONST
#from .modelsConstants import *
from .models import accessoAtti
from .forms import accessoAttiForm
#from .serializers import UserListSerializer

# Create your views here.
@csrf_exempt
def access_create(request):
    if request.method == "POST":
        cu = accessoAttiForm(request.POST)
        if cu.is_valid():
            cu.save()
            return "Record saved correctly"           
    return False

def access_list_all(request):
    if request.method == "GET":
        accessList = list(accessoAtti.objects.all())
        #serialize it so the JSON can be returned
        accessList = serializers.serialize('json', accessList)
        return JsonResponse({"data": accessList}, safe=False)          
    