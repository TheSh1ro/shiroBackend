from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


from core.models import Modalidade
from core.serializers import ModalidadeSerializer

class ModalidadeViewSet(ModelViewSet):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

class ModalidadeList(generics.ListCreateAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

class ModalidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer
