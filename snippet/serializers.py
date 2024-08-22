from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    highlighted = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # snippets identifier comes from related_name
    # now when i access the user then insted of nested snippit object that user has it will have pk of them
    snippetss = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippetss"]
