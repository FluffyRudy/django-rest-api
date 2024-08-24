from django.http import HttpRequest, JsonResponse, HttpResponse, Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import APIView, api_view, action
from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.reverse import reverse
from .serializers import SnippetSerializer, UserSerializer
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from .permissions import IsOwnerOrReadOnly


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )


class SnippetViewSet(viewsets.ModelViewSet):
    """this provide `list` `create` `retrive` `update` `delete`(destroy) acction automatically
    additionally we provide extra `highlight` action too
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """viewset that provide list and retrive actions automatically"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LanguageList(APIView):
    def get(self, request, *args, **kwargs):
        languages = [item[0] for item in LANGUAGE_CHOICES]
        paginator = PageNumberPagination()
        paginated_language = paginator.paginate_queryset(languages, request)
        return paginator.get_paginated_response(paginated_language)


class StyleChoices(APIView):
    def get(self, request, *args, **kwargs):
        styles = [item[0] for item in LANGUAGE_CHOICES]
        paginator = PageNumberPagination()
        paginated_style = paginator.paginate_queryset(styles, request)
        return paginator.get_paginated_response(paginated_style)


class SnippetHyperlink(APIView):
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        paginator = PageNumberPagination()
        paginated_snippets = paginator.paginate_queryset(snippets, request)
        serializer = SnippetSerializer(
            paginated_snippets, many=True, context={"request": request}
        )
        snippet_urls = [snippet["url"] for snippet in serializer.data]
        return paginator.get_paginated_response(snippet_urls)
