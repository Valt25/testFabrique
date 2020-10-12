from django.contrib.auth import authenticate
from rest_framework import serializers

from rest_framework.exceptions import ValidationError


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=255)
    password = serializers.CharField(required=True, max_length=255)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        user = authenticate(username=username, password=password)

        if user:
            attrs['user'] = user
            return attrs
        else:
            raise ValidationError("User is not authenticated")


