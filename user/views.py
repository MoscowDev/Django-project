from django.contrib.auth.forms import UserCreationForm
from rest_framework import status

from .serializers import UserSerializer
from .serializers import LoginSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.onboarding_services import create_user_and_wallet
# Create your views here.

@api_view(['POST'])
def register(request):
  serializer = UserSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  create_user_and_wallet(serializer.validated_data)
  return Response({"messsage": "Registration successful"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.validated_data, status=status.HTTP_200_OK)
