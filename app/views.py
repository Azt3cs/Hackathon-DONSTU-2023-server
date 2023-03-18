
from django.http import HttpResponse
from django.shortcuts import render

from .serializers import *
from rest_framework import generics
from .models import *


class PariAPIView(generics.ListAPIView):
    queryset = Pari.objects.all()
    serializer_class = PariSerializer

class GroupPairList(generics.ListAPIView):
    serializer_class = PariSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        group = Group.objects.get(name=group_id)
        return Pari.objects.filter(group=group)

class PrepodPairList(generics.ListAPIView):
    serializer_class = PariSerializer

    def get_queryset(self):
        prepod_id = self.kwargs['prepod_id']
        prepod = Prepodi.objects.get(fio=prepod_id)
        return Pari.objects.filter(prepod=prepod)
class GroupAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
