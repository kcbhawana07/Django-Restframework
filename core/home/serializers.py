from rest_framework import serializers
from .models import * 


class StudentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # field=['name','age']#for selected name ,age
        # exclude=['id',]#for remove id 
        fields='__all__'#for seleecting all models

        def validate(self,data):
            if data["age"]<18:
                raise serializers.ValidationError({"error":"age cannot be less than 18"})
            
            return data
        

class CategorySerilazier(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class BookSerilazier(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


        