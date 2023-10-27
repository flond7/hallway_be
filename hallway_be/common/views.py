from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import UserLoginSerializer

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
        if serializer.is_valid():
            logger.info('valid serial')
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                logger.info(f'Before login: User {user.username} ({user.id}) is being logged in.')
                login(request, user)
                logger.info(f'After login: User {user.username} ({user.id}) has been logged in successfully.')
        
                logger.info(login)
                data = {'data': 'Login effettuato', 'status': 201}
                return JsonResponse(data, status=201)
            else:
                logger.info('user is none')
                data = {'data': 'Utente non autorizzato (utente vuoto)', 'status': 401}
                return JsonResponse(data, status=401)
        else:
            logger.error(serializer.errors)  
            data = {'data': 'Problema con il serializer che risulta invalido', 'status': 201}
            return JsonResponse(data, status=400)
