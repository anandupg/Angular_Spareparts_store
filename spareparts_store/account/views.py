from urllib import request
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import users
from .serializers import UsersSerializer
from django.contrib.auth.hashers import check_password

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Please provide both email and password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = users.objects.get(email=email)
        except users.DoesNotExist:
            try:
                user = users.objects.get(username=email)
            except users.DoesNotExist:
                return Response(
                    {"error": "Invalid Credentials"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if check_password(password, user.password):
            return Response({
                "message": "Login Successful", 
                "user": {
                    "id": str(user.id),
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            }, status=status.HTTP_200_OK)

        else:
            return Response(
                {"error": "Invalid Credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )
