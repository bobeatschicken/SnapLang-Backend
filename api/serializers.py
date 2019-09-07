from rest_framework import serializers
from .models import Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("english_definition", "foreign_definition")

    def update(self, instance, validated_data):
        instance.english_definition = validated_data.get(
            "english_definition", instance.english_definition)
        instance.foreign_definition = validated_data.get(
            "foreign_definition", instance.foreign_definition)
        instance.save()
        return instance
