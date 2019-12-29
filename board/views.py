from django.shortcuts import render, redirect
from rest_framework import viewsets
# from .serializers import HobbySerializer
# from .models import Hobby
from .models import Paper

# class HobbyViewSet(viewsets.ModelViewSet):
#     queryset = Hobby.objects.all()
#     serializer_class = HobbySerializer


def listFBV(request):
    papers = Paper.objects.all()
    return render(request, 'board/index.html', {'papers':papers})