from django.contrib.auth.models import User
from .serializers import LogSerializer
from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey
from license_plate_recognition.models import Log

class CreateLog(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [HasAPIKey]