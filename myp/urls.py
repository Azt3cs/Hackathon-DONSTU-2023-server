
from django.contrib import admin
from django.urls import path, include

from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PariAPIView.as_view()),
    path('group/',GroupAPIView.as_view()),
    path('groups/<slug:group_id>/pairs/', GroupPairList.as_view(), name='group-pair-list'),
    path('prepod/<slug:prepod_id>/pairs/', PrepodPairList.as_view()),
]

