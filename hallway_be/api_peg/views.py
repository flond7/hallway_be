from django.shortcuts import render
from django.http import JsonResponse
#from rest_framework.response import Response
#from rest_framework import status
import json

from .models import goalPeg
from .forms import goalPegForm
from .serializers import goalPegSerializer, goalPegCreateSerializer

from api_user.models import PAOffice, PAUser

import logging
logger = logging.getLogger(__name__)

# CORS
from django.views.decorators.csrf import csrf_exempt
""" 
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
 """
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
                office__id=idOffice,
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

@csrf_exempt
def create_multiple_goals(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Log the request data for debugging
            logger.info(data)
            serializer = goalPegCreateSerializer(data=data, many=True)
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
def delete_multiple_goals(request):
    if request.method == 'DELETE':
        try:
            logger.info(request.body)  # Log the request data for debugging
            data = json.loads(request.body)
            logger.info(data)  # Log the request data for debugging

            for goal_id in data:
                try:
                    goal = goalPeg.objects.get(pk=goal_id)
                    goal.delete()
                except goalPeg.DoesNotExist:
                    return JsonResponse({"data": f"Goal with ID {goal_id} does not exist"}, status=400)

            return JsonResponse({"data": "Records have been deleted"}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {str(e)}")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return JsonResponse({"error": "An error occurred while deleting goals"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_multiple_goals(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            logger.info(data)  # Log the request data for debugging
            
            # goals_data = data.get("goals", [])  # Assuming 'goals' is the key in your JSON data

            for goal_data in data:
                goal_id = goal_data.get("id") 
                try:
                    goal = goalPeg.objects.get(pk=goal_id)

                    # Update the fields of the goal based on the incoming data
                    # Example: assuming 'name' and 'description' can be updated
                    goal.name = goal_data.get("name", goal.name)
                    goal.description = goal_data.get("description", goal.description)
                    goal.year = goal_data.get("year", goal.year)
                    
                    # get object before assignment
                    officeId = goal_data.get("office", goal.office)
                    office_object = PAOffice.objects.get(pk=officeId)
                    goal.office = office_object

                    # get object before assignment
                    managerId = goal_data.get("manager", goal.manager)
                    manager_object = PAUser.objects.get(pk=managerId)
                    goal.manager = manager_object
                    
                    goal.weight = goal_data.get("weight", goal.weight)
                    goal.percent_3006 = goal_data.get("percent_3006", goal.percent_3006)
                    goal.weight_3006 = goal_data.get("weight_3006", goal.weight_3006)
                    goal.percent_3112 = goal_data.get("percent_3112", goal.percent_3112)
                    goal.weight_3112 = goal_data.get("weight_3112", goal.weight_3112)
                    goal.type = goal_data.get("type", goal.name)

                    #goal.involvedPeople = goal_data.get("involvedPeople", goal.involvedPeople)
                    involved_people_data = goal_data.get("involvedPeople", [])
                    goal.involvedPeople.set(involved_people_data)
  
                    goal.save()  # Save the updated goal
                except goalPeg.DoesNotExist:
                    # Handle case where the goal with that ID doesn't exist
                    return JsonResponse({"data": "Il record che stai cercando di aggiornare non esiste"}, status=400)
                    pass

            return JsonResponse({"data": "Goals updated successfully"}, status=200)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return JsonResponse({"error": "An error occurred while updating goals"}, status=400)
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
