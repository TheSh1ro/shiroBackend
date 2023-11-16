from rest_framework import serializers
from rest_framework import generics

from core.models import Modalidade

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__'

class ModalidadeList(generics.ListCreateAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer
