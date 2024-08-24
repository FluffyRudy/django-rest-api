from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.api_root),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user-detail"),
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path(
        "snippets/<int:pk>/highlight/",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    path("snippet-urls", views.SnippetHyperlink.as_view(), name="snippet-urls"),
    path("languages/", views.LanguageList.as_view(), name="languages"),
    path("styles/", views.LanguageList.as_view(), name="styles"),
    path("accounts/profile/", views.UserProfileView.as_view(), name="user-profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [path("api-auth/", include("rest_framework.urls"))]
