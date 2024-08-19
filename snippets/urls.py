from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.redirect_snippet_list, name="home"),
    path("snippets/", views.snippets_list, name="snippets"),
    path("snippets/<int:pk>/", views.snippedt_detail, name="snippet-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
