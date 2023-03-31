from .models import customUser, askUser
from rest_framework import serializers

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser,
        fields = ('name', 'surname')