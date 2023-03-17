from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import *


class PariAPIView(generics.ListAPIView):
    queryset = Pari.objects.all()
    serializer_class = PariSerializer
