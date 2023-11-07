from .models import goalPeg
from api_user.serializers import PAOfficeSerializer
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class goalPegSerializer(serializers.ModelSerializer):
    offices = PAOfficeSerializer(many=True, read_only=True)

    class Meta:
        model = goalPeg
        fields = '__all__'