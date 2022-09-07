from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer, TaskSerializer
from api.models import Task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



@method_decorator(csrf_exempt, name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['patch', 'post' ]

    def update(self, request, pk=None):
        user = request.user
        instance = self.get_object()
        for i in range(1,5):
            data = {
                "TotalIterations": i,
                "Status": 'IN-PROGRESS'
            }
        
            serializer = self.serializer_class(instance=instance,
                                            data=data, # or request.data
                                            context={'author': user},
                                            partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)