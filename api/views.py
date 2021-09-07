from django.contrib.auth.models import User
from .serializers import LogSerializer
from license_plate_recognition.models import Log
from rest_framework import generics

class CreateLog(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer