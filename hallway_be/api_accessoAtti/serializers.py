from .models import accessoAtti
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class accessoAttiSerializer(serializers.ModelSerializer):
    class Meta:
        model = accessoAtti
        fields = '__all__'