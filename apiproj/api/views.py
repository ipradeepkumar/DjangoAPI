from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from api.serializers import TaskSerializer
from api.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def GetAllTasks(request):
    serialzer = TaskSerializer(Task.objects.all(), many = True, context={'request': request})
    return Response(data = serialzer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
def PostTask(request):
    instance = Task.objects.get(pk=request.data["GUID"])
    ProcessTask(instance=instance)
    return Response(status=status.HTTP_200_OK)

async def ProcessTask(instance): 
    for i in range(instance.TotalIterations):
            data = {
                "TotalIterations": i,
                "Status": 'IN-PROGRESS'
            }
            serializer = TaskSerializer(instance=instance, data=data)
            if serializer.is_valid():
                isValid = True
                serializer.save()
    if (i == instance.TotalIterations - 1):
        compData = {
            "Status": 'COMPLETED'
        }
        compSerializer = TaskSerializer(instance=instance, data=compData)
        if compSerializer.is_valid():
            compSerializer.save()
    return isValid      

