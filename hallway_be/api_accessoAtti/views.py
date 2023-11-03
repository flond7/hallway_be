from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework import status
import json

# CORS
from django.views.decorators.csrf import csrf_exempt



# MY VARS
#from .constants import MY_CONST
#from .modelsConstants import *
from .models import accessoAtti
from .forms import accessoAttiForm
from .serializers import accessoAttiSerializer




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
                return JsonResponse({"data": "Record saved correctly", 'status': 200}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def access_list_all(request):
    if request.method == "GET":
        # retrieve all the data in the form of a ueryset
        accessList = accessoAtti.objects.all()
        # transform the queryset in a data type that can be rendered as json trough a serializer
        serializer = accessoAttiSerializer(accessList, many=True)
        # transform the serialized data in a json and send them
        return JsonResponse({"data": serializer.data}, safe=False)

@csrf_exempt
def access_delete(request, pk):
    try:
        record = accessoAtti.objects.get(pk=pk)
    except accessoAtti.DoesNotExist:
        data = {'data': 'Questo accesso non è registrato sul database', 'status': 404}
        return JsonResponse(data, status=404)
        #return Response(status=status.HTTP_404_NOT_FOUND)
    record.delete()
    #return Response(status=status.HTTP_204_NO_CONTENT)
    data = {'data': 'I dati sono stati cancellati correttamente', 'status': 201}
    return JsonResponse(data, status=201)


