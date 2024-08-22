from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"

    def get_initial(self):
        initial = super().get_initial() or {}
        initial["language"] = Snippet._meta.get_field("language").get_default()
        initial["style"] = Snippet._meta.get_field("style").get_default()
        print(initial)
        return initial
