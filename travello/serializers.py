from rest_framework import serializers
from .models import Destination

class destSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Destination
        #  fields = ('name')
        fields = '__all__'   # for all fields 