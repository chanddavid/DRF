from django.urls import path
from . import views

urlpatterns = [
    path("get_api/", views.get_api.as_view()),
    path("get_api/<int:id>/", views.get_api.as_view()),
]
