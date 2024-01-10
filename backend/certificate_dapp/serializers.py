# todos/serializers.py
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'address',
            'private_key',
            'created',
            
        )
        model = Account

