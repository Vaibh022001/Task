from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ProjectCreateSerializer
from django.shortcuts import get_object_or_404

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'], url_path='projects')
    def create_project(self, request, pk=None):
        client = get_object_or_404(Client, pk=pk)
        serializer = ProjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save(client=client, created_by=request.user)
        project.users.set(serializer.validated_data['users'])
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

class UserProjectViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        projects = request.user.assigned_projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
