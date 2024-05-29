# serializers.py
from django.contrib.auth import authenticate
from rest_framework import serializers

class SuperuserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user and user.is_superuser:
                data['user'] = user
            else:
                raise serializers.ValidationError('Invalid credentials or not a superuser.')
        else:
            raise serializers.ValidationError('Both fields are required.')

        return data