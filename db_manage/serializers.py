from dataclasses import field
from db_manage.models import DBmanageModel
from rest_framework import serializers

class DBmanageModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = DBmanageModel
        fields = '__all__'

