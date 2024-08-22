from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username"
    )  # read only so unwriteable explicitly and is hidden

    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style", "owner"]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )  # define reverse relation with with uesr and snippet means user can access snippet indirectly

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]  # fields to allow in serializer
