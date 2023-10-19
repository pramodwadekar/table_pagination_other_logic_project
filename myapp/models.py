from django.db import models
from django.contrib import admin 

class student(models.Model):   
    Fullname = models.CharField(max_length=50)
    DOB = models.DateField()
    Email = models.EmailField(max_length=50)
    Age = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Qualification =models.CharField(max_length=50)
    Subject = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Fullname
    
    # change DataBase Name
    class Meta: 
        # Add Table Name
        db_table = ''
        # Add verbose name 
        verbose_name = 'Student Management System'
        verbose_name_plural = "Student Management System'"







    
