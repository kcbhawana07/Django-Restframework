from rest_framework import serializers
from models import * 


class StudntSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        field=['name','age']
        exclude=['id',]
        field='__all__'