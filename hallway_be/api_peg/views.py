from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
#from rest_framework import status
import json

from .models import goalPeg
from .forms import goalPegForm
from .serializers import goalPegSerializer

import logging
logger = logging.getLogger(__name__)

# CORS
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def goal_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            g = goalPegForm(data)
            if g.is_valid():
                g.save()
                return JsonResponse({"data": "Record saved correctly", 'status': 200}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


""" @csrf_exempt
def create_multiple_goals(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(data)  # Log the request data for debugging
            data = json.loads(request.body)
            serializer = goalPegSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data": "Record saved correctly", 'status': 200}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
 """
@csrf_exempt
def create_multiple_goals(request):
    if request.method == 'POST':
        try:
            data = request.body  # Log the request data for debugging
            logger.info(data)
            serializer = goalPegSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data": "Records saved correctly"}, status=201)
            else:
                logger.error(serializer.errors)  # Log validation errors for debugging
                return JsonResponse({"error": "Invalid data", "details": serializer.errors}, status=400)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return JsonResponse({"error": "An error occurred"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)

