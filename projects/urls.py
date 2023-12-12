# projects/urls.py

# Import path
from django.urls import path
from .views import project_list

# Url patterns
urlpatterns = [
    path('', project_list, name='project_list'),
]
