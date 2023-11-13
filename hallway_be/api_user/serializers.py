from .models import customUser, askUser, PAUser, PAOffice
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ('id', 'name', 'surname', 'jobCategory')


class PAOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAOffice
        fields = '__all__'


class ManagerForOfficeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = PAUser
        fields = ('id', 'name', 'surname')

class PAOfficeAndPOSerializer(serializers.ModelSerializer):
    manager = ManagerForOfficeSerialzer(source='get_manager', read_only=True)

    class Meta:
        model = PAOffice
        fields = ('id', 'name', 'manager')


# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class PAUserPEGSerializer(serializers.ModelSerializer):
    managerOfOffices = PAOfficeSerializer(many=True, read_only=True)

    class Meta:
        model = PAUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'manager', 'managerOfOffices')