from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from .models import UserProfile
from .serializers import UserLoginSerializer, UserProfileSerializer

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

@csrf_exempt
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

@csrf_exempt
def user_log(request):
    if request.method == 'POST':
        #get the data in a format that the serializer can handle
        data = json.loads(request.body.decode('utf-8'))
        serializer = UserLoginSerializer(data=data)
        #logger.info(request.META)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            logger.info('serializer is valid')
            logger.info(user)
            if user is not None:
                login(request, user)
                data = {'data': 'Login effettuato', 'userid': user.id, 'status': 201}
                return JsonResponse(data, status=201)
            else:
                data = {'data': 'Utente non autorizzato', 'status': 401}
                return JsonResponse(data, status=401)
        else:
            logger.error(serializer.errors)  
            data = {'data': 'Problema con il serializer che risulta invalido', 'status': 201}
            return JsonResponse(data, status=400)

def get_user_profiles_auth(request, pk):
    if request.method == "GET":
        try:
            auth = UserProfile.objects.get(pk=pk)
            # Convert the UserProfile object to a dictionary so the serializer can use it
            auto_for_serializer = model_to_dict(auth)
            logger.info(auto_for_serializer)
            data = {'data': auto_for_serializer, 'status': 201}
            return JsonResponse(data, status=201)
        except UserProfile.DoesNotExist:
            return JsonResponse({"error": "Profilo utente non trovato"}, status=404)

