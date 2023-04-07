from .models import customUser, askUser
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ('name', 'surname', 'jobCategory')