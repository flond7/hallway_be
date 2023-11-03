from .models import customUser, askUser, PAUser, PAOffice
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'manager', 'managerOffice')


# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class PAUserPEGSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'manager', 'managerOffice')

class PAOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAOffice
        fields = '__all__'