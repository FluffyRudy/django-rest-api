from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.redirect_snippets),
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>", views.SnippetDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),
    path("languages/", views.LanguageList.as_view()),
    path("themes/", views.StyleList.as_view()),
]

urlpatterns += [path("api-auth", include("rest_framework.urls"))]
