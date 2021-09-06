from rest_framework import serializers
from license_plate_recognition.models import Log

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('plate_number', 'offence', 'image',)