from django.urls import path
from .views import register, login_user
from .views import ResourceList


urlpatterns = [
    path('register/', register),
    path('login/', login_user),
    path('resources/', ResourceList.as_view()),
]
