from django.urls import path
from Web_app.view import master,humanresource,dashboard
urlpatterns = [

#DashBoard
path('', dashboard.Dashboard, name="dashboard"),

#human resource
path('human_resource/', humanresource.Human_resource,name="human_resource"),
path('attendance/', humanresource.Attendance,name="attendance"),
path('datewise_atend/', humanresource.Datewise_Atendance,name="datewise_atendance"),

path('attendance_list/', humanresource.Attendance_List,name="attendance_list"),
path('monthwise_atend/', humanresource.Monthwise_Atendance,name="monthwise_atendance"),

#master
path('master/',master.Master,name="master"),
path('employee/',master.Employee,name="employee"),

path('employee_list/',master.Employee_list,name="employee_list"),
path('employee_lists/',master.Employee_lists,name="employee_lists"),
path('employee_edit/<int:employee_id>',master.Employee_edit,name="employee_edit"),
path('employee_delete/<int:employee_id>',master.Employee_Delete, name='employee_delete'),
path('employee_filter/', master.Employee_filter,name='employee_delete'), 

path('branch/',master.Branch, name='branch'),
path('branch_edit/<int:branch_id>', master.Branch_Edit,name="branch_edit"),
path('branch_delete/<int:branch_id>', master.Branch_Delete, name='branch_delete'),
path('branch_filter/', master.Branch_filter, name='branch_filter'), 

path('designation/', master.Designation, name='designation'),
path('designation_edit/<int:designation_id>', master.Designation_Edit,name="designation_edit"),
path('designation_delete/<int:designation_id>', master.Designation_Delete, name='designation_delete'),

]