from rest_framework import serializers
from .models import *

# create your serializers here 

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'