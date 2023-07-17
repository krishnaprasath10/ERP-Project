from django.db import models
from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt

class log_entrys_api(models.Model):
    time_entry = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    trace_back=models.CharField(max_length=200,null=True,blank=True)
    IP_address=models.CharField(max_length=200,blank=True,null=True)
    path=models.CharField(max_length=200,blank=True,null=True)
    
class Department(models.Model):
    Department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Department
    
class Designation(models.Model):
    Designation = models.CharField(max_length=100)   

    def __str__(self):
        return self.Designation
    
class Branch(models.Model):
    Branch = models.CharField(max_length=100)
    Is_Head = models.BooleanField(default=False)
    Location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Branch
    
    
class Employee_Details(models.Model):
    Employee_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_Of_Birth = models.CharField(max_length=100)
    Blood_Group = models.CharField(max_length=100)
    Date_Of_Joining = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100,null=True)
    Email_Id = models.CharField(max_length=100)
    Department = models.ForeignKey("Department",on_delete=models.SET_NULL, null=True) 
    Designation = models.ForeignKey("Designation",on_delete=models.SET_NULL, null=True) 
    Qualification = models.CharField(max_length=100)
    Current_Address = models.CharField(max_length=100)
    Permanent_Address =models.CharField(max_length=100)
    Aadhar_Number = models.IntegerField(null=True)
    Pan_Number = models.CharField(max_length=100, null=True)
    EPF_Number = models.CharField(max_length=100, null=True)
    
    Previous_Experience = models.CharField(max_length=100)
    Experience_years = models.IntegerField(null=True)
    Reference_Through = models.CharField(max_length=100 ,null=True)
    Previous_Company_Name = models.CharField(max_length=100,null=True)
    Reference_Name = models.CharField(max_length=100 ,null=True)
    Branch = models.ForeignKey("Branch",on_delete=models.SET_NULL, null=True) 
    
    Bank_Name = models.CharField(max_length=100)
    Account_Number = models.IntegerField(null=True)
    Account_Holder_Name = models.CharField(max_length=100)
    IFSC_Code =models.CharField(max_length=100)
    Branch_Name =models.CharField(max_length=100)
    
    Salary_Type = models.CharField(max_length=100)
    Basic_Pay = models.IntegerField(null=True)
    Working_Hours = models.IntegerField(null=True)
    Casual_Leave_Permonth = models.IntegerField(null=True)
    HRA = models.IntegerField(null=True)
    Medical_Allowence = models.IntegerField(null=True)
    Conveyance_Allowence = models.IntegerField(null=True)
    General_Allowence = models.IntegerField(null=True)
    Professional_Tax =models.IntegerField(null=True)
    RD = models.IntegerField(null=True)
    PF =models.IntegerField(null=True)
    ESI = models.IntegerField(null=True)
    Net_Salary = models.IntegerField(null=True)

    def __str__(self):
        return self.Employee_Name

class Attendance(models.Model):
    
    PRESENT = 'Present'
    ABSENT = 'Absent'
    CASUAL = 'Casual'
    SICK = 'Sick'
    
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (CASUAL, 'Casual'),
        (SICK, 'Sick'),
    ]
    
    Date = models.DateField(null=True)
    Employee_Name = models.ForeignKey("Employee_Details",on_delete=models.SET_NULL, null=True) 
    Working_Hours = models.IntegerField(null=True)
    Worked_Hours = models.IntegerField(null=True)
    Over_Time = models.IntegerField(null=True)
    Permission = models.IntegerField(null=True)
    Casual_Leave = models.IntegerField(null=True)
    Sick_Leave = models.IntegerField(null=True)
    Status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)

    

