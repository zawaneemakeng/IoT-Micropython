from rest_framework import serializers
from .models import TempHumid


class TempHumidSerializer(serializers.ModelSerializer):
    class Meta:
        # ตรวจสอบข้อมูล
        model = TempHumid
        fields = ('id', 'code', 'title', 'temperature', 'humidity')
