from rest_framework.views import APIView
from rest_framework.response import Response
from Api_app.serializers import*
from rest_framework import status
from Api_app.models import*
from datetime import datetime
from Api_app.log import function_api_log

class EmployeeCreate(APIView):
    def post(self, request):
        try:
            serializer = Employee_Details_Serializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save()
                return Response({'data': serializer.data,},status=status.HTTP_201_CREATED) 
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmployeeGet(APIView):
    def get(self, request):
        employees = Employee_Details.objects.all()
        serializer = Employee_Details_Serializer(employees, many=True)
        #print(serializer.data)
        return Response(serializer.data)
    
class Employee_id_Get(APIView):
    def get(self, request, employee_id):
        try:
            employee = Employee_Details.objects.get(id=employee_id)
            serializer = Employee_Details_Serializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({"error": "Employee not found."},status=status.HTTP_404_NOT_FOUND)
    
class EmployeeDelete(APIView):
    def delete(self, request, employee_id):
        try:
            employee = Employee_Details.objects.get(id=employee_id)
            employee.delete()
            return Response({'message': 'Employee Deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

class EmployeeEdit(APIView):
    def put(self, request):
        try:
            employee_id = request.GET.get('id')
            print('----------', employee_id)
            
            employee_data = Employee_Details.objects.get(id=employee_id)
            print('==========', employee_data)
            
            serializer = Employee_Details_Serializer(instance=employee_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("ok")
                return Response(serializer.data, status=status.HTTP_200_OK)
            print("OOOOOOO")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
         
class DepartmentCreate(APIView):
    def post(self, request):
        try:
            serializer = Department_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data,},status=status.HTTP_201_CREATED)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DepartmentGet(APIView):
    def get(self, request):
        department = Department.objects.all()
        serializer = Department_Serializer(department, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class Department_Filter(APIView):
    def get(self, request):
        department = request.GET.get('departments')  
        print(department)
       
        filtered_department = Employee_Details.objects.all()
        filtered_departments = filtered_department.filter(Department=department)            
        serializer = Employee_Details_Serializer(filtered_departments, many=True)
       # print(response_data)
        return Response(serializer.data)
    
class DesignationCreate(APIView):
    def post(self, request):
        try:
            serializer = Designation_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data,},status=status.HTTP_201_CREATED) 
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesignationGet(APIView):
    def get(self, request):
        designation = Designation.objects.all()
        serializer = Designation_Serializer(designation, many=True)
        #print(serializer.data)
        return Response(serializer.data)
    
class Designation_id_Get(APIView):
    def get(self, request, designation_id):
        try:  
            designation = Designation.objects.get(id=designation_id)
            serializer = Designation_Serializer(designation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({"error": "Designation not found."},status=status.HTTP_404_NOT_FOUND)
    
class DesignationDelete(APIView):
    def delete(self, request, designation_id):
        try:
            designation = Designation.objects.get(id=designation_id)
            designation.delete()
            return Response({'message': 'Designation  Deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'message': 'Designation not found'}, status=status.HTTP_404_NOT_FOUND)
        
class BranchCreate(APIView):
    def post(self, request):
        try:
            serializer = Branch_Serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data,},status=status.HTTP_201_CREATED) 
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BranchGet(APIView):
    def get(self, request):
        branch = Branch.objects.all()
        serializer = Branch_Serializer(branch, many=True)
        #print(serializer.data)
        return Response(serializer.data)
    
class Branch_id_Get(APIView):
    def get(self, request, branch_id):
        try:
            branch = Branch.objects.get(id=branch_id)
            
            serializer = Branch_Serializer(branch)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({"error": "Branch not found."},status=status.HTTP_404_NOT_FOUND)
    
class BranchDelete(APIView):
    def delete(self, request, branch_id):
        try:
            branch = Branch.objects.get(id=branch_id)
            branch.delete()
            return Response({'message': 'Branch  Deleted Succesfully'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            function_api_log(request,str(e),e)
            return Response({'message': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
        
class Branch_Filter(APIView):
    def get(self, request):
        branch = request.GET.get('branchs') 
        print(branch)
        filtered_branch = Employee_Details.objects.all()
        filtered_branchs = filtered_branch.filter(Branch=branch) 
        serializer = Employee_Details_Serializer(filtered_branchs, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
