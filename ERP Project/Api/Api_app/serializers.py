from rest_framework import serializers
from .models import *


class Department_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'
        
class log_entrys_api_serializer(serializers.ModelSerializer):
    class Meta:
        model=log_entrys_api
        fields= '__all__' 
        
class Employee_Details_Serializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='Department.Department')
    branch_n = serializers.ReadOnlyField(source='Branch.Branch')
    designation_name = serializers.ReadOnlyField(source='Designation.Designation')
    

    class Meta:
        model = Employee_Details
        fields = ['id','Employee_Name','Gender','Date_Of_Birth','Blood_Group','Date_Of_Joining','Phone_Number','Email_Id','Designation','designation_name',
                  'Department','department_name','Qualification','Current_Address','Permanent_Address','Aadhar_Number','Pan_Number','EPF_Number',
                  'Previous_Experience','Experience_years','Reference_Through','Previous_Company_Name','Reference_Name','Branch','branch_n','Bank_Name',
                  'Account_Number','Account_Holder_Name','IFSC_Code','Branch_Name','Salary_Type','Basic_Pay','Working_Hours',
                  'Casual_Leave_Permonth','HRA','Medical_Allowence','Conveyance_Allowence','General_Allowence','Professional_Tax','RD','PF','ESI',
                  'Net_Salary']

class Designation_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Designation
        fields = '__all__'

class Branch_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Branch
        fields = '__all__'
        
class Attendance_Details_Serializer(serializers.ModelSerializer):
    Employee_Name_name = serializers.ReadOnlyField(source='Employee_Name.Employee_Name')

    class Meta:
        model = Attendance
        fields =  ['id','Date','Employee_Name','Employee_Name_name','Working_Hours','Worked_Hours','Over_Time','Permission','Casual_Leave',
                   'Sick_Leave','Status',]
        
        
class Datewise_Attendance_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee_Details
        fields = ['id', 'Employee_Name', 'Working_Hours']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        date = self.context.get('Date')
        data['Date'] = date
        attendance_query = Attendance.objects.filter(Employee_Name=instance.id, Date=date)
        
        if attendance_query.exists():
            attendance_data = {}
            for attendance in attendance_query:
                attendance_serializer = Attendance_Details_Serializer(attendance)
                attendance_data.update(attendance_serializer.data)
            data['Attendance'] = attendance_data
        else:
            
            attendance_data = {'Status':'-NA-','Worked_Hours':0,'Over_Time':0,'Permission':0,'Casual_Leave':0,'Sick_Leave':0}
            for attendance in attendance_query:
                attendance_serializer = Attendance_Details_Serializer(attendance)
                attendance_data.update(attendance_serializer.data)
            data['Attendance'] = attendance_data
        return data



        
class MonthwiseAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Details
        fields = ['id', 'Employee_Name', 'Working_Hours'] 

    def to_representation(self, instance):
            data = super().to_representation(instance)
            month = self.context.get('Month')
            year = self.context.get('Year')
            attendance_query = Attendance.objects.filter(Employee_Name=instance.id, Date__month=month, Date__year=year).order_by('Date')

            if attendance_query.exists():
                attendance_data = {}
                for attendance in attendance_query:
                    attendance_serializer = Attendance_Details_Serializer(attendance)
                    date = attendance_serializer.data['Date']
                    attendance_data[date] = attendance_serializer.data
                sorted_attendance_data = dict(sorted(attendance_data.items(), key=lambda x: x[0]))
                data['Attendance'] = sorted_attendance_data
            else:
                attendance_data = {'-NA-': {'Status': '-NA-'}}
                data['Attendance'] = attendance_data
            return data
       