from django.urls import path
from Api_app.view import humanresource,master

urlpatterns = [
#Master
        path('employee_create/', master.EmployeeCreate.as_view()),
        path('employee_get/', master.EmployeeGet.as_view()),
        path('employee_id_get/<int:employee_id>/', master.Employee_id_Get.as_view()),
        path('employee/delete/<int:employee_id>/', master.EmployeeDelete.as_view()),
        path('employee/edit/', master.EmployeeEdit.as_view()),
              
        path('department_create/', master.DepartmentCreate.as_view()),
        path('department_get/', master.DepartmentGet.as_view()),
        path('employee/department_filter/', master.Department_Filter.as_view()),
        
        path('branch_create/', master.BranchCreate.as_view()),
        path('branch_get/', master.BranchGet.as_view()),
        path('branch_id_get/<int:branch_id>/', master.Branch_id_Get.as_view()),
        path('branch/delete/<int:branch_id>/', master.BranchDelete.as_view()),
        path('employee/branch_filter/', master.Branch_Filter.as_view()),

        path('designation_create/', master.DesignationCreate.as_view()),
        path('designation_get/', master.DesignationGet.as_view()),
        path('designation_id_get/<int:designation_id>/', master.Designation_id_Get.as_view()),
        path('designation/delete/<int:designation_id>/', master.DesignationDelete.as_view()),

#Human_Resources
        path('attendance/get/', humanresource.Attendance_Get.as_view()),
        path('datewise_attendance/', humanresource.Datewise_attendance.as_view()),
        path('monthwise_attendance/', humanresource.MonthwiseAttendance.as_view()),
        path('attendance/', humanresource.Attendances.as_view()),

]