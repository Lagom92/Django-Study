from django.shortcuts import render, redirect
from rest_framework import viewsets
# from .serializers import HobbySerializer
# from .models import Hobby
from django.views.generic import ListView
from .models import Paper

# class HobbyViewSet(viewsets.ModelViewSet):
#     queryset = Hobby.objects.all()
#     serializer_class = HobbySerializer

# FBV list
def listFBV(request):
    papers = Paper.objects.all()
    return render(request, 'board/index.html', {'papers':papers})

# CBV list
class listCBV(ListView):
    model = Paper

# default 설정 변경 - CBV list
class listCBV2(ListView):
    template_name = 'board/index.html'
    context_object_name = 'papers'
    model = Paper

# 컨텍스트 오버라이딩
class listCBV3(ListView):
    def get_queryset(self):
        return Paper.objects.all()

