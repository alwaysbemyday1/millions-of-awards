from rest_framework import serializers

from core.models import MajorCategory, MinorCategory

class MajorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorCategory
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

class MinorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MinorCategory
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}