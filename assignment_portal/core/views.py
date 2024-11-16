from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User, Assignment
from .serializers import UserSerializer, AssignmentSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'Login successful', 'user_id': user.id})
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class AssignmentView(APIView):
    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Assignment uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminAssignmentsView(APIView):
    def get(self, request, admin_id):
        assignments = Assignment.objects.filter(admin_id=admin_id)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

class UpdateAssignmentStatusView(APIView):
    def post(self, request, assignment_id):
        status = request.data.get('status')
        assignment = Assignment.objects.get(id=assignment_id)
        assignment.status = status
        assignment.save()
        return Response({'message': f'Assignment {status.lower()} successfully'})
