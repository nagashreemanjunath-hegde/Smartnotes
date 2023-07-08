from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pmk>', views.DetailView.as_view()),
]