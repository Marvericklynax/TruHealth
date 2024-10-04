from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from .models import Resource
from .serializers import ResourceSerializer

# Resource List view
class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Resource List Create View (make sure this is defined)
class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# User registration view
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': {'message': 'Username and password are required'}}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': {'message': 'Username already taken'}}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
    except ValidationError as e:
        return Response({'error': {'messages': list(e.messages)}}, status=status.HTTP_400_BAD_REQUEST)

# User login view
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': {'message': 'Username and password are required'}}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    
    return Response({'error': {'message': 'Invalid credentials'}}, status=status.HTTP_401_UNAUTHORIZED)
