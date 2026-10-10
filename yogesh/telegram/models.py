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