from rest_framework import serializers

from core.models import Fila

class FilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fila
        fields = '__all__'
