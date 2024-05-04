from rest_framework import serializers
from .models import ModelMalfunctions


class MalfunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMalfunctions
        fields = (
            'address',
            'num_house',
            'entrance',
            'flat_or_tel',
            'dispatcher',
            'date_time_accepted',
            'mechanics',
            'date_time_transfer',
            'malfunction_and_cause',
            'date_time_closed',
            'simple',
            'executor_mechanics',
            'description',
            'status',
        )
