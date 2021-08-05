from rest_framework import serializers 
from apirest.models import logTres
 
 
class logTresSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = logTres
        fields = ('id', 'date_created', 'key', 'value')
