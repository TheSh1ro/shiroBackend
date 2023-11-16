from rest_framework import serializers

from core.models import Elo

class EloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elo
        fields = '__all__'
