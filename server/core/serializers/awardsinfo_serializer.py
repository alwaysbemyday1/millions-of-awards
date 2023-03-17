from rest_framework import serializers

from core.models import AwardsInfo

class AwardsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsInfo
        fields = '__all__'

