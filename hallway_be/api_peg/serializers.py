from .models import goalPeg
from api_user.serializers import PAOfficeSerializer, PAUserPEGSerializer
from api_user.models import PAOffice, PAUser
from rest_framework import serializers

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class goalPegSerializer(serializers.ModelSerializer):
    office = PAOfficeSerializer(many=False, read_only=True)
    manager = PAUserPEGSerializer(many=False, read_only=True)

    class Meta:
        model = goalPeg
        fields = ('id', 'year', 'office','name','description','weight', 'manager', 'percent_3006', 'weight_3006', 'percent_3112', 'weight_3112', 'type','involvedPeople')

# This is used to create or update elements 
class goalPegCreateSerializer(serializers.ModelSerializer):
    office = serializers.PrimaryKeyRelatedField(queryset=PAOffice.objects.all())  # Assuming 'PAOffice' is your office model
    manager = serializers.PrimaryKeyRelatedField(queryset=PAUser.objects.all())  # Assuming 'PAUser' is your user model

    class Meta:
        model = goalPeg
        fields = ('id', 'year', 'office', 'name', 'description', 'weight', 'manager', 'percent_3006', 'weight_3006', 'percent_3112', 'weight_3112', 'type', 'involvedPeople')
