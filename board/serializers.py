from rest_framework import serializers
from .models import Hobby

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('id', 'title', 'maker', 'content')