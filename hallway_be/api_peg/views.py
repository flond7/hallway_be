from django.shortcuts import render
from django.http import JsonResponse
#from rest_framework.response import Response
#from rest_framework import status
import json

from .models import goalPeg
from .forms import goalPegForm
from .serializers import goalPegSerializer

from api_user.models import PAOffice

import logging
logger = logging.getLogger(__name__)

# CORS
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_person_results(request, name):
    if request.method == "GET":
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

@csrf_exempt
def get_person_results(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  # Access the 'year' field from the JSON data
            idPerson = data['id']
            goalList = goalPeg.objects.filter(
                involvedPeople__id=idPerson,
                year=year
            )
            serializer = goalPegSerializer(goalList, many=True)
            return JsonResponse({"data": serializer.data}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def get_po_results(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  # Access the 'year' field from the JSON data
            idPerson = data['id']
            goalList = goalPeg.objects.filter(
                manager__id=idPerson,
                year=year
            )
            serializer = goalPegSerializer(goalList, many=True)
            return JsonResponse({"data": serializer.data}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def get_office_results(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  # Access the 'year' field from the JSON data
            idOffice = data['id']
            goalList = goalPeg.objects.filter(
                office__id=idPerson,
                year=year
            )
            serializer = goalPegSerializer(goalList, many=True)
            return JsonResponse({"data": serializer.data}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def goal_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            g = goalPegForm(data)
            if g.is_valid():
                g.save()
                # Get the ID of the newly created record
                new_record_id = g.id
                logger.info(g.id)
                logger.info('g.id')
                return JsonResponse({"id": new_record_id, 'status': 200}, status=200)
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
            data = json.loads(request.body)  # Log the request data for debugging
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


@csrf_exempt
def get_goals_numbers(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  # Access the 'year' field from the JSON data

            # Get a list of all offices in the database
            offices = PAOffice.objects.all()

            # Initialize a list to store the goal counts for each office
            data = []

            for office in offices:
                # Filter goals by year and office
                ordinary_goals = goalPeg.objects.filter(year=year, office=office.id, type="ordinary").count()
                extraordinary_goals = goalPeg.objects.filter(year=year, office=office.id, type="extraordinary").count()
                
                # Create a nested dictionary for each office
                office_data = {
                    "ordinary": ordinary_goals,
                    "extraordinary": extraordinary_goals,
                    "name": office.name
                }

                # Store the counts in the dictionaries
                data.append(office_data)

            return JsonResponse(data, status=200, safe=False)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
