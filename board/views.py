from rest_framework import viewsets
from .serializers import HobbySerializer
from .models import Hobby

class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


