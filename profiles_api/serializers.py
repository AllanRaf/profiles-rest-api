from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers validate field"""
    """Serializes a name field for testing our APIViews"""

    name = serializers.CharField(max_length=10)
