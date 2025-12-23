from rest_framework import serializers
from .models import * 


class StudentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # field=['name','age']#for selected name ,age
        # exclude=['id',]#for remove id 
        fields='__all__'#for seleecting all models
        