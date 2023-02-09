from .models import ParsedData
from rest_framework import serializers


class ParsedDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParsedData
        fields = ['text', 'tag', 'date', 'photo_path']
