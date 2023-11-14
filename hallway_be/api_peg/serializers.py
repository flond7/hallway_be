from .models import goalPeg
from api_user.serializers import PAOfficeSerializer, PAUserPEGSerializer
from api_user.models import PAOffice, PAUser
from rest_framework import serializers


class goalPegSerializer(serializers.ModelSerializer):
    office = PAOfficeSerializer(many=False, read_only=True)
    manager = PAUserPEGSerializer(many=False, read_only=True)

    """ def update(self, instance, validated_data):
        # Handle the many-to-many field separately
        involved_people_data = validated_data.pop('involvedPeople', None)

        if involved_people_data is not None:
            # Check if the list is not empty before calling set
            if involved_people_data:
                instance.involvedPeople.set(involved_people_data)
            else:
                # If the list is empty, clear the existing relationships
                instance.involvedPeople.clear()

        # Perform the default update
        return super(goalPegSerializer, self).update(instance, validated_data) """

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
