from .models import goalPeg
from api_user.serializers import PAOfficeSerializer
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class goalPegSerializer(serializers.ModelSerializer):
    office = PAOfficeSerializer(many=False, read_only=True)

    class Meta:
        model = goalPeg
        fields = ('id', 'year', 'office','name','description','weight', 'manager', 'percent_3006', 'weight_3006', 'percent_3112', 'weight_3112', 'type','involvedPeople')