from rest_framework import serializers
from .models import Home, About,Service,Testimonails


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonails
        fields = "__all__"