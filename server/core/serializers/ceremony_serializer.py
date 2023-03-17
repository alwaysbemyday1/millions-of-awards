from rest_framework import serializers

from core.models import Ceremony

class CeremonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = '__all__'