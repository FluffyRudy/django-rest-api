from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"
        extra_kwargs = {
            "language": {"default": "python"},
            "style": {"default": "monokai"},
        }  # default laguage and style
