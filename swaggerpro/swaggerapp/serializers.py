from rest_framework import serializers
from swaggerapp.models import patient_detail
class patient_serializer(serializers.ModelSerializer):
    class Meta:
        model=patient_detail
        fields='__all__'
