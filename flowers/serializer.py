from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Flowers


class  FlowersSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Flowers
        fields = ('name','description','user','created_at','updated_at' )