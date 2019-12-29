from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('listFBV/', views.listFBV, name="list"),
]