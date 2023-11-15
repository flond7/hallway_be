from .models import goalPeg
from api_user.serializers import PAOfficeSerializer, PAUserPEGSerializer
from api_user.models import PAOffice, PAUser
from rest_framework import serializers


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

    def update(self, instance, validated_data):
        # Update the existing instance with the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.office = validated_data.get('office', instance.office)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.percent_3006 = validated_data.get('percent_3006', instance.percent_3006)
        instance.weight_3006 = validated_data.get('weight_3006', instance.weight_3006)
        instance.percent_3112 = validated_data.get('percent_3112', instance.percent_3112)
        instance.weight_3112 = validated_data.get('weight_3112', instance.weight_3112)
        instance.type = validated_data.get('type', instance.type)
        instance.involvedPeople.set(validated_data.get('involvedPeople', instance.involvedPeople.all()))

        instance.save()
        return instance

    class Meta:
        model = goalPeg
        fields = ('id', 'year', 'office', 'name', 'description', 'weight', 'manager', 'percent_3006', 'weight_3006', 'percent_3112', 'weight_3112', 'type', 'involvedPeople')
