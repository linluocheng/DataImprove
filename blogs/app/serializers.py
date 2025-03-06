from rest_framework import serializers
from .models import Login,Information

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ["username",'password']

class InforSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ["name","infor"]
