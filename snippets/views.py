from django.http import HttpRequest, JsonResponse, HttpResponse, Http404
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect
from .serializers import SnippetSerializer
from .models import Snippet
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


def redirect_snippet_list(request):
    return redirect("snippets")


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]  # auth=rw, unauth=r
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer: SnippetSerializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]  # same as above
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
