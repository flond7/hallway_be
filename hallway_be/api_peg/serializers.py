from .models import goalPeg
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class goalPegSerializer(serializers.ModelSerializer):
    class Meta:
        model = goalPeg
        fields = '__all__'