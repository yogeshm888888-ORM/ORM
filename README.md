# Ex02 Django ORM Web Application
## Date: 12.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```

models.py
from django.db import models
from django.contrib import admin
class Vehicle_DB(models.Model):
    service_ID=models.IntegerField()
    Customer_Name=models.CharField(max_length=50)
    Vehicle_Number=models.CharField(max_length=10)
    Vehicle_Model=models.CharField(max_length=50)
    Contact_Number=models.IntegerField()
    Service_Cost=models.FloatField()
    Address=models.TextField()
class Vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["service_ID","Customer_Name","Vehicle_Number","Vehicle_Model","Contact_Number","Service_Cost","Address"]

admin.py
from django.contrib import admin
from .models import Vehicle_DB,Vehicle_DBAdmin
admin.site.register(Vehicle_DB,Vehicle_DBAdmin)


```

## OUTPUT
![alt text](<Screenshot 2026-10-10 093121.png>)



## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
