from rest_framework_mongoengine import serializers
from inventory.models import Category,Part

class PartSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Part
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

class CategorySerializer(serializers.DocumentSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)
        
