from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json

# CORS
from django.views.decorators.csrf import csrf_exempt



# MY VARS
#from .constants import MY_CONST
#from .modelsConstants import *
from .models import accessoAtti
from .forms import accessoAttiForm
#from .serializers import UserListSerializer




import logging
logger = logging.getLogger(__name__)



# Create your views here.
""" @csrf_exempt
def access_create(request):
    aa = accessoAttiForm()
    #aa = json.loads(request.body)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {e}")
    return JsonResponse({"error": "Invalid JSON data"}, status=400)  # Return a bad request response
    logger.error(f"JSON parsing error: {e}")
    if request.method == "POST":
        #aa = accessoAttiForm(request.POST)
        aa = accessoAttiForm(json.loads(request.body))
        logger.debug(f"Received POST data: {request.body}")
        if aa.is_valid():
            aa.save()
            return JsonResponse({"data": "Record saved correctly"}, safe=False)           
    return False """

@csrf_exempt
def access_create(request):
    aa = accessoAttiForm()
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            aa = accessoAttiForm(data)
            if aa.is_valid():
                aa.save()
                return JsonResponse({"data": "Record saved correctly"}, safe=False)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


def access_list_all(request):
    if request.method == "GET":
        accessList = list(accessoAtti.objects.all())
        #serialize it so the JSON can be returned
        accessList = serializers.serialize('json', accessList)
        return JsonResponse({"data": accessList}, safe=False)          
    