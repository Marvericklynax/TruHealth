from django.urls import path
from .views import ResourceList, register, login_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('resources/', ResourceList.as_view(), name='resource-list'),
]
