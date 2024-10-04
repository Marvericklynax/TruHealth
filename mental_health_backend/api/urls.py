from django.urls import path
from .views import register, login_user, ResourceList, ResourceListCreateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('resources/', ResourceList.as_view(), name='resource-list'),  # For listing resources
    path('resources/create/', ResourceListCreateView.as_view(), name='resource-create'),  # For creating resources
]
