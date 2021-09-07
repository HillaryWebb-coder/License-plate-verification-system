from rest_framework import serializers
from license_plate_recognition.models import Log
from rest_flex_fields import FlexFieldsModelSerializer

class LogSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Log
        fields = ['image',]