from rest_framework import status
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser , IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from .models import CustomUser
from django.views.decorators.http import require_GET
from django.db import connection
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        # Your registration logic
         # If the email is already registered, return an error response
        elif CustomUser.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'Email is already registered.'}, status=status.HTTP_400_BAD_REQUEST)
        # If the username is already taken, return an error response
        elif CustomUser.objects.filter(username=request.data.get('username')).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({"message":"Incorrect password"}, status=status.HTTP_400_BAD_REQUEST) 
        
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return Response("User deleted successfully", status=status.HTTP_204_NO_CONTENT)

class HealthCheckView(View):
    def get(self, request):
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            db_status = 'OK'
        except Exception as e:
            db_status = str(e)

        # Add more checks if necessary

        # Create a health status dictionary
        health_status = {
            'database': db_status,
            'health': 'Application is healthy' 
        }
        # Return the health status as a JSON response
        return JsonResponse(health_status)