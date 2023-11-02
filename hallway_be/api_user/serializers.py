from .models import customUser, askUser, PAUser
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'responsable', 'responsableOffice')


# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class PAUserPEGSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'responsable', 'responsableOffice')