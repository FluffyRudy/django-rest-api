from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.redirect_snippet_list, name="home"),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),
    path("snippets/", views.SnippetList.as_view(), name="snippets"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path("accounts/profile/", views.UserProfileView.as_view(), name="user-profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [path("api-auth/", include("rest_framework.urls"))]
