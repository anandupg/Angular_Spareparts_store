from rest_framework_mongoengine import serializers
from .models import users
from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.DocumentSerializer):
    class Meta:
        model = users
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data) 