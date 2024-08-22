from django.urls import path
from . import views

urlpatterns = [
    path("", views.SnippetList.as_view()),
    path("snippet/<int:pk>", views.SnippetDetail.as_view()),
]
