from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Import for a simple landing page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='landing'),  # Add this line for the landing page
    path('api/', include('api.urls')),  # Ensure your API URLs are included
    path('mental_health/', include('mental_health.urls')),  # Include your app's URLs
]
