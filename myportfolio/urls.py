# myportfolio/urls.py

# Import django admin and urls
from django.contrib import admin
from django.urls import include, path

# Url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('blog/', include('blog.urls')),
]
