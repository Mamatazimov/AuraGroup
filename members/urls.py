from django.urls import path
from .views import *




urlpatterns = [
    path('', MembersListView.as_view(), name='member-list'),
]
