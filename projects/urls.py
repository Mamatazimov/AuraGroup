from django.urls import path
from .views import *




urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
]



