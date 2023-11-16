from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


from core.models import Servico
from core.serializers import ServicoSerializer 

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoList(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
