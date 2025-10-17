from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        # Alternatively, specify fields explicitly
        # fields = ['id', 'name', 'description', 'price', 'selection']