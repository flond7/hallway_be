from django.shortcuts import render

from .models import obbiettivoPeg
from .forms import obbiettivoPegForm
from .serializers import obbiettivoPegSerializer

# Create your views here.

@csrf_exempt
def goal_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            g = obbiettivoPegForm(data)
            if aa.is_valid():
                g.save()
                return JsonResponse({"data": "Record saved correctly", 'status': 200}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
