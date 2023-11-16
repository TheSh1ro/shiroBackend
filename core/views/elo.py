from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


from core.models import Elo
from core.serializers import EloSerializer

class EloViewSet(ModelViewSet):
    queryset = Elo.objects.all()
    serializer_class = EloSerializer

class EloList(generics.ListCreateAPIView):
    queryset = Elo.objects.all()
    serializer_class = EloSerializer

class EloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Elo.objects.all()
    serializer_class = EloSerializer
