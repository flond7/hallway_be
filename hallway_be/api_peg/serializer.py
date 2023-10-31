from .models import obbiettivoPeg
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class obbiettivoPegSerializer(serializers.ModelSerializer):
    class Meta:
        model = obbiettivoPeg
        fields = '__all__'