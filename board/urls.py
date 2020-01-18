from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('listFBV/', views.listFBV, name="list"),
    path('listCBV/', views.listCBV.as_view()),
    path('listCBV2/', views.listCBV2.as_view()),
    path('listCBV3/', views.listCBV3.as_view()),
]