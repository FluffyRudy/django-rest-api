from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from .serializers import SnippetSerializer
from .serializers import UserSerializer
from .models import Snippet, LANGUAGES, STYLES
from .permissions import isOwnerOrReadOnly


def redirect_snippets(request):
    return redirect("snippets/")


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    # to restrict content based on user
    #     user: User = self.request.user
    #     if user.is_authenticated:
    #         return Snippet.objects.filter(owner=user)
    #     return Snippet.objects.none()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    # def get_queryset(self):
    #     user: User = self.request.user
    #     if user.is_authenticated:
    #         return Snippet.objects.filter(owner=user)
    #     return Snippet.objects.none()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LanguageList(APIView):
    def get(self, request, *args, **kwargs):
        print(LANGUAGES)
        return Response({"languages": [item[0] for item in LANGUAGES]})


class StyleList(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"styles": [item[0] for item in STYLES]})
