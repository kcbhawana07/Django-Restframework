from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    father_name=models.CharField(max_length=100)


class Category(models.Model):
    category_name=models.CharField()

class Book(models.Model):
    category=models.CharField()
    book_title=models.CharField()



    
