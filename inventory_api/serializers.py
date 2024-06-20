from rest_framework import serializers
from .models import Item


class ItemRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "description", "quantity", "price"]


class ItemResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "description",
            "quantity",
            "price",
            "created_at",
            "updated_at",
        ]
