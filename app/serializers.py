from rest_framework import serializers
from .models import *
class PariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pari
        fields =('predmet','prepod','date','auditoria','group')

