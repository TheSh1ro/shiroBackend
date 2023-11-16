from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


from core.models import Fila
from core.serializers import FilaSerializer

class FilaViewSet(ModelViewSet):
    queryset = Fila.objects.all()
    serializer_class = FilaSerializer

class FilaList(generics.ListCreateAPIView):
    queryset = Fila.objects.all()
    serializer_class = FilaSerializer

class FilaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fila.objects.all()
    serializer_class = FilaSerializer
