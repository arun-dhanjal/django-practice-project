from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_app, name='practice-question'),
]
