from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserProfileSerializer(serializers.Serializer):
    user = User  # Include the UserSerializer for the 'user' field

    class Meta:
        model = UserProfile
        fields = '__all__'