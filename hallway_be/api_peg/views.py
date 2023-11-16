from django.shortcuts import render
from django.http import JsonResponse
import json

# REST FRAMEWORK
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status

# IMPORTS from APP
from .models import goalPeg
from .forms import goalPegForm
from .serializers import goalPegSerializer, goalPegCreateSerializer
from api_user.models import PAOffice, PAUser

# LOGGING
import logging
logger = logging.getLogger(__name__)

# STATS and AVARAGE
import statistics
from django.db.models import Count, Sum, F
from operator import itemgetter

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
def get_person_min_results(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  # Access the 'year' field from the JSON data
            id_person = data['id']

            goal_list = goalPeg.objects.filter(
                involvedPeople__id=id_person,
                year=year
            )

            # divide the list in ordinary and extraordinary
            ordinary_list = goal_list.filter(type='ordinary')
            extraordinary_list = goal_list.filter(type='extraordinary')

            # Count the number of ordinary and extraordinary goals
            ordinary_count = ordinary_list.count()
            extraordinary_count = extraordinary_list.count()

            # Calculate the percentage of realization for ordinary and extraordinary goals
            total_weight_ordinary = ordinary_list.aggregate(total_weight=Sum('weight'))['total_weight'] or 0
            total_weight_extraordinary = extraordinary_list.aggregate(total_weight=Sum('weight'))['total_weight'] or 0
            total_weight_all = total_weight_ordinary + total_weight_extraordinary

            if total_weight_all > 0:
                percent_realization_ordinary = (total_weight_ordinary / total_weight_all) * 100
                percent_realization_extraordinary = (total_weight_extraordinary / total_weight_all) * 100
            else:
                percent_realization_ordinary = 0
                percent_realization_extraordinary = 0

            # Get user information
            user_info = PAUser.objects.filter(id=id_person).values('name', 'surname', 'jobCategory').first()

            response_data = {
                "ordinary_count": ordinary_count,
                "extraordinary_count": extraordinary_count,
                "name": user_info['name'],
                "surname": user_info['surname'],
                "jobCategory": user_info['jobCategory'],
                "percent_ordinary": percent_realization_ordinary,
                "percent_extraordinary": percent_realization_extraordinary
            }

            return JsonResponse({"data": response_data}, status=200)

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
@parser_classes([JSONParser])
def update_multiple_goals(request):
    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            errors = []

            for goal_data in data:
                goal_id = goal_data.get("id")

                try:
                    goal = goalPeg.objects.get(pk=goal_id)
                except goalPeg.DoesNotExist:
                    goal = None  # Goal doesn't exist, it will be created

                serializer = goalPegCreateSerializer(instance=goal, data=goal_data)

                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.append(serializer.errors)

            if errors:
                return JsonResponse({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse({"data": "Goals updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)

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

            # Initialize an empty dic to store people's numbers (and count how many people are involved)
            people_involved = {}

            for office in offices:
                # Get all the goals in for the office
                goals_for_office = goalPeg.objects.filter(year=year, office=office)

                # get the list divided in ordinary and extraordinary
                ordinary_list = goals_for_office.filter(type="ordinary")
                extraordinary_list = goals_for_office.filter(type="extraordinary")

                # Filter goals by year and office
                ordinary_goals = ordinary_list.count()
                extraordinary_goals = extraordinary_list.count()

                # Get the total weight and the weight at 31/12 so you can calculate the percentage in FE
                sum_weights = sum(goal.weight for goal in goals_for_office)
                sum_weights3006 = sum(goal.weight_3006 for goal in goals_for_office)
                sum_weights3112 = sum(goal.weight_3112 for goal in goals_for_office)

                sum_extra_weights = sum(goal.weight for goal in extraordinary_list)
                sum_extra_weights3006 = sum(goal.weight_3006 for goal in extraordinary_list)
                sum_extra_weights3112 = sum(goal.weight_3112 for goal in extraordinary_list)
                
                sum_ord_weights = sum(goal.weight for goal in ordinary_list)
                sum_ord_weights3006 = sum(goal.weight_3006 for goal in ordinary_list)
                sum_ord_weights3112 = sum(goal.weight_3112 for goal in ordinary_list)

                # Iterate in involvedPeople to add every person involved and count how many times they are involved in a goal
                for goal in goals_for_office:
                    for person in goal.involvedPeople.all():
                        person_id = person.id

                        # Increment the count for this person
                        people_involved[person_id] = people_involved.get(person_id, 0) + 1

                # Create a nested dictionary for each office
                office_data = {
                    "ordinary": ordinary_goals,
                    "extraordinary": extraordinary_goals,
                    "name": office.name,
                    "sum_extra_weights": sum_extra_weights,
                    "sum_extra_weights3006": sum_extra_weights3006,
                    "sum_extra_weights3112": sum_extra_weights3112,
                    "sum_ord_weights": sum_ord_weights,
                    "sum_ord_weights3006": sum_ord_weights3006,
                    "sum_ord_weights3112": sum_ord_weights3112,
                    "sum_weights": sum_weights,
                    "sum_weights3006": sum_weights3006,
                    "sum_weights3112": sum_weights3112,
                }

                # Store the counts in the dictionaries
                data.append(office_data)

                # create the object to return
                returnData = {
                    'data': data,
                    'people_involved': people_involved
                }


            return JsonResponse(returnData, status=200, safe=False)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def check_existing_goals(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']  
            office_id = data['officeId']
            records_exist = goalPeg.objects.filter(office_id=office_id, year=year).exists()
            return JsonResponse(records_exist, status=200, safe=False)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def get_average_weight(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            year = data['year']
            records = goalPeg.objects.filter(year=year)

            if not records.exists():
                return JsonResponse({"error": "No records found for the given year"}, status=404)

            # Dictionary to store the total weight and count for each person
            person_weights = {}

            for record in records:
                involved_people = record.involvedPeople.all()
                for person in involved_people:
                    if person.id not in person_weights:
                        person_weights[person.id] = {'total_weight': 0, 'count': 0}

                    person_weights[person.id]['total_weight'] += record.weight
                    person_weights[person.id]['count'] += 1

            # Calculate the average weight, itemgetter retrieves total weight, map iterates iteemgetter in all the elements of person weights, and sum sums all the values retrieved
            sum_weights = sum(map(itemgetter('total_weight'), person_weights.values()))
            num_people = len(person_weights)
            avarage = sum_weights / num_people

            # Calculate standard deviation: get the series and then use the statistic function
            total_weights = [item['total_weight'] for item in person_weights.values()]
            std_deviation = statistics.stdev(total_weights)


        
            return JsonResponse({"average_weight": avarage, 'standard_deviation': std_deviation}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


