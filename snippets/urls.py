from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_snippet_list, name="home"),
    path("snippets/", views.snippets_list, name="snippets"),
    path("snippets/<int:pk>/", views.snippedt_detail, name="snippet-detail"),
]
