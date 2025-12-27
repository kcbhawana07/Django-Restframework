from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student,Book,Category
from .serializers import StudentSerilaizer,BookSerilazier,CategorySerilazier,UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import generics
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
    

@api_view(['GET'])
def get_book(request):
    book_obj=Book.objects.all()
    serializer=BookSerilazier(book_obj,many=True)
    return Response({"status":200,"playload":serializer.data})


@api_view(['GET'])
def get_category(request):
    category_obj=Category.objects.all()
    serializer=CategorySerilazier(category_obj,many=True)
    return Response({"status":200,"playload":serializer.data})


@api_view(['GET'])
def get_student(request):
    student_obj=Student.objects.all()
    serializer=StudentSerilaizer(student_obj,many=True)
    return Response({"status":200,"playload":serializer.data})









class StudentAPI(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass
    def put(self,request):
        pass
    def patch(self,request):
        pass
    def delete(self,request):
        pass


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    


from rest_framework.authentication import TokenAuthentication
class RegisterUser(APIView):
    def post(self,request):
     serializer=UserSerializer(data=request.data)

     if not serializer.is_valid():
         print(serializer.errors)
         return Response({"status":403,"error":serializer.errors,"message":"user token authentication"})
     
     serializer.save()
     user=User.objects.get(username=serializer.data['username'])
     token_obj=Token.objects.get_or_create(user=user)
     return Response({"status":200,"token":str(token_obj),"playload":serializer.data,"message":"save your data"})



class GenericView(generics.ListAPIView,generics.CreateAPIView):
    queryset=Student.objects.all() 
    serializer_class=StudentSerilaizer

class GenericDelete(generics.DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilaizer
    lookup_field="id"







