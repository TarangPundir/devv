from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from .serializers import TeacherSerializer

# Create your views here.
@api_view(['GET'])
def List(request):
    teacher = Teacher.objects.all()
    serialized = TeacherSerializer(teacher, many=True)
    return Response([serialized.data])

@api_view(['GET'])
def view(request, id):
    teacher = Teacher.objects.get(id=id)
    serialized = TeacherSerializer(teacher)
    return Response([serialized.data])

@api_view(['POST'])
def create(request):
    teacher = Teacher.objects.all()
    serialized = TeacherSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(['success'])
    
@api_view(['DELETE'])
def delete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response(["success"])

@api_view(['PUT'])
def update(request, id):
    teacher = Teacher.objects.get(id=id)
    serializedOne = TeacherSerializer(teacher)
    serialized = TeacherSerializer(teacher, data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response([serializedOne.data])