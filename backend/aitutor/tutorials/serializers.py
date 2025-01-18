from rest_framework import serializers
from .models import Language, ColorScheme


class ColorSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorScheme
        fields = ['primary_color', 'secondary_color', 'background_color', 'text_color', 'accent_color']


class LanguageSerializer(serializers.ModelSerializer):
    color_scheme = ColorSchemeSerializer(read_only=True)

    class Meta:
        model = Language
        fields = ['id', 'name', 'description', 'code_example', 'color_scheme']
