from rest_framework.views import APIView
from rest_framework.response import Response
from Api_app.serializers import*
from rest_framework import status
from Api_app.models import*
from datetime import datetime
from Api_app.log import function_api_log

class Attendances(APIView):
    def post(self, request):
        try:
            serializer = Attendance_Details_Serializer(data=request.data)
            
            if serializer.is_valid():
                date = serializer.validated_data['Date']
                employee_name = serializer.validated_data['Employee_Name']
                
                attendance_qs = Attendance.objects.filter(Date=date, Employee_Name=employee_name)
                
                if attendance_qs.exists():
                    attendance = attendance_qs.first()
                    serializer = Attendance_Details_Serializer(attendance, data=request.data)
                    
                    if serializer.is_valid():
                        serializer.save()
                        print(serializer.data)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    serializer.save()
                    print(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Attendance_Get(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = Attendance_Details_Serializer(attendance, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class Datewise_attendance(APIView):
    def get(self, request):
        dates = request.GET.get('date') 
        
        context = {
        'Date': dates, 
        }
        print(context)
        employees =Employee_Details.objects.all()
        serializer = Datewise_Attendance_Serializer(employees, many=True, context=context)
        #print(serializer.data)
        return Response(serializer.data)
   

class MonthwiseAttendance(APIView):
    def get(self, request):
        month_year = request.GET.get('month_year')     
        try:
            date_obj = datetime.strptime(month_year, '%m-%Y')
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'error': 'Invalid month_year format. Please use MM-YYYY.'}, status=400)

        month = date_obj.month
        year = date_obj.year

        context = {
            'Month': month,
            'Year': year, 
        }
        print(context)
        
        employees = Employee_Details.objects.all()
        serializer = MonthwiseAttendanceSerializer(employees, many=True, context=context)
        return Response(serializer.data)
