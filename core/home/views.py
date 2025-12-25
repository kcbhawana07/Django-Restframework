from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerilaizer
# Create your views here.

@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()
    serializer=StudentSerilaizer(student_obj,many=True)
    return Response ({"status":200,"message":'Hello from django rest framework','payload':serializer.data})


@api_view(['POST'])
def post_student(request):
    serializer=StudentSerilaizer(data=request.data)

    if request.data['age']<18:
        return Response({"status":403,"message":"age must be >18"})
      
    if not serializer.is_valid():
        print(serializer.errors)
    return Response({'status':403,"error":serializer.errors,"message":'you sent'})



@api_view(['DELETE'])
def delete(request):
    student_obj=Student.objects.all()
    serializer=StudentSerilaizer(student_obj,many=True)
    return Response ({"status":200,"message":'Hello from django rest framework for deleted','payload':serializer.data})


@api_view(['PUT'])
def update_student(request,id):
    try:
        student_obj=Student.objects.all(id=id)
        serializer=StudentSerilaizer(data=request.data)
        if not serializer.is_valid():
         print(serializer.errors)
        return Response ({"status":200,'errors':serializer.errors,"message":'Hello from django rest framework for updates '})
    
        serializer.save()
        return Response({"status":200,"playload":serializer.data}) 
    
    except Exception as e:
        return Response({"status":403,"message":"invalid id"})








