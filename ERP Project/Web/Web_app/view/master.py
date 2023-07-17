from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
from django.contrib import messages


def Master(request):
    emp_lst = 'http://127.0.0.1:8000/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
    count = len(Emp)
    #print("+++++++++++++++++",count)
    return render(request, "Master/master.html",{"count":count})


#Branch
def Branch(request):

    branch = 'http://127.0.0.1:8000/branch_get/'
    get_response = requests.get(branch)
    branch_lst = get_response.json()
    if request.method == 'POST':
        data = {
            'Branch' :  request.POST.get("branch"),
            'Is_Head' : request.POST.get("is_head"),
            'Location': request.POST.get("location"),                
        }
        print(data)
        response = requests.post('http://127.0.0.1:8000/branch_create/', data=data)
        if response.status_code == 201:
            data = response.json()
            print(data)
            messages.success(request,"Branch Succesfully Created")
            return redirect('branch')
        else:    
               
            print("++++++++ error")  
            err = response.status_code
            print(err)
            messages.error(request,"Branch Not Created..!")
            return render(request, "Master/master.html")
    return render(request,"Master/branch.html",{'branch_lst':branch_lst})

def Branch_Edit(request, branch_id):
    branch = f'http://127.0.0.1:8000/branch_id_get/{branch_id}/'
    get_response = requests.get(branch)
    branchs = get_response.json()
    print(branchs)
    return render(request,'Master/branch.html',{'branchs':branchs})
    
def Branch_Delete(request, branch_id):
    delete_branch = f'http://127.0.0.1:8000/branch/delete/{branch_id}/'
    get_response = requests.delete(delete_branch)
    return redirect('branch')

def Branch_filter(request):
     
    branch = request.POST.get('branchs')
    url = 'http://127.0.0.1:8000/employee/branch_filter/'
    params = {
        'branchs': branch,
    }
    response = requests.get(url, params=params)
    print(branch)
    if response.status_code == 200:
        print(response.json())
        return JsonResponse(response.json(), safe=False)
    
    else:
        print('Error:', response.status_code)
        return JsonResponse(response, safe=False)

#Designation
def Designation(request):
    designation = 'http://127.0.0.1:8000/designation_get/'
    get_response = requests.get(designation)
    designation_lst = get_response.json()
    if request.method == 'POST':
        data = {
            'Designation' :  request.POST.get("designation"),               
        }
        print(data)
        response = requests.post('http://127.0.0.1:8000/designation_create/', data=data)
        if response.status_code == 201:
            data = response.json()
            print(data)
            messages.success(request,"Designation Succesfully Created")
            return redirect('designation')
        else:       
            print("++++++++ error")  
            err = response.status_code
            print(err)
            messages.error(request,"Designation Not Created..!")
            return render(request, "Master/designation.html")
    return render(request,"Master/designation.html",{'designation_lst':designation_lst})

def Designation_Edit(request, designation_id):
    designation = f'http://127.0.0.1:8000/designation_id_get/{designation_id}/'
    get_response = requests.get(designation)
    designations = get_response.json()
    print(designations)
    return render(request,'Master/branch.html',{'designations':designations})
    
  
def Designation_Delete(request, designation_id):
    delete_designation = f'http://127.0.0.1:8000/designation/delete/{designation_id}/'
    get_response = requests.delete(delete_designation)
    return redirect('designation')

#Employees
def Employee(request):
    messages.success(request, 'Employee Created Succesfull.')
    department = 'http://127.0.0.1:8000/department_get/'
    get_response = requests.get(department)
    depart = get_response.json()
    branch = 'http://127.0.0.1:8000/branch_get/'
    get_respons = requests.get(branch)
    branch_lst = get_respons.json()
    designation = 'http://127.0.0.1:8000/designation_get/'
    get_response = requests.get(designation)
    designation_lst = get_response.json()
    if request.method == 'POST':
        data = {
            
            "Employee_Name": request.POST.get("employee_name"),
            "Gender":  request.POST.get("gender"),
            "Date_Of_Birth": request.POST.get("dob"),
            "Blood_Group": request.POST.get("blood"),
            "Date_Of_Joining": request.POST.get("doj"),
            "Phone_Number": request.POST.get("phone"),
            "Email_Id": request.POST.get("email"),
            "Department": request.POST.get("department"),
            "Designation": request.POST.get("designation"),
            "Qualification": request.POST.get("qualification"),
            "Current_Address":request.POST.get("cur_address"),
            "Permanent_Address":request.POST.get("Per_address"),
            "Aadhar_Number": request.POST.get("aadhar"),
            "Pan_Number": request.POST.get("pan"),
            "EPF_Number":request.POST.get("EPF"),
            
            "Previous_Experience": request.POST.get("experience"), 
            "Experience_years" : request.POST.get("experience_years"),
            "Reference_Through"  : request.POST.get("reference_through"),
            "Previous_Company_Name"  : request.POST.get("previous_Company_name"),
            "Referece_Name" : request.POST.get("reference_name"),
            "Branch"  : request.POST.get("branch"),
            
            "Bank_Name" : request.POST.get("bank_name"),
            "Account_Number": request.POST.get("account_number"),
            "Account_Holder_Name": request.POST.get("account_holder_name"),
            "IFSC_Code": request.POST.get("ifsc"),
            "Branch_Name" : request.POST.get("branch_name"),
            
            "Salary_Type": request.POST.get("salary_type"),
            "Basic_Pay" : request.POST.get("basic_pay"),
            "Working_Hours" : request.POST.get("working_hours"),
            "Casual_Leave_Permonth" : request.POST.get("casual_leave_per_month"),
            "HRA" : request.POST.get("hra"),
            "Medical_Allowence" : request.POST.get("medical_allowence"),
            "Conveyance_Allowence": request.POST.get("conveyance_allowence"),
            "General_Allowence": request.POST.get("general_allowence"),
            "Professional_Tax": request.POST.get("professional_tax"),
            "RD" : request.POST.get("rd"),
            "PF" : request.POST.get("pf"),
            "ESI" : request.POST.get("esi"),
            "Net_Salary" : request.POST.get("net_salary")
                    
        }
        print(data)
        response = requests.post('http://127.0.0.1:8000/employee_create/', data=data)
   
        if response.status_code == 201:
            data = response.json()
            print(data)
            return redirect( "employee_list")
        
   
        else:       
            print("++++++++ error")  
            err = response.status_code
            print(err)
            return render(request, "Master/employee.html")
    
    #print(depart)
    return render(request, "Master/employee.html",{"depart":depart,'branch_lst':branch_lst,'designation_lst':designation_lst})

#Employee List
def Employee_list(request):
    url = 'http://127.0.0.1:8000'
    emp_lst = f'{url}/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
    department = f'{url}/department_get/'
    get_response = requests.get(department)
    depart = get_response.json()
    print(Emp)
    return render(request, "Master/employee_list.html",{"emp_lst":Emp,"depart":depart})
    
def Employee_lists(request):
    url = 'http://127.0.0.1:8000'
    emp_lst = f'{url}/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
   
    return JsonResponse(Emp, safe=False)
    
def Employee_Delete(request, employee_id):
    delete_data = f'http://127.0.0.1:8000/employee/delete/{employee_id}/'
    get_response = requests.delete(delete_data)
    return redirect('employee_list')

def Employee_edit(request, employee_id):
    department = 'http://127.0.0.1:8000/department_get/'
    get_response = requests.get(department)
    depart = get_response.json()
    branch = 'http://127.0.0.1:8000/branch_get/'
    get_respons = requests.get(branch)
    branch_lst = get_respons.json()
    designation = 'http://127.0.0.1:8000/designation_get/'
    get_response = requests.get(designation)
    designation_lst = get_response.json()
    emp_get_url = f'http://127.0.0.1:8000/employee_id_get/{employee_id}/'
    put_url = f'http://127.0.0.1:8000/employee/edit/'

    if request.method == "GET":
        emp_lst = emp_get_url
        get_response = requests.get(emp_lst)
        Emp = get_response.json()
        #print(Emp)
        return render(request, "Master/employee_edit.html",{"emp_lst":Emp,"depart":depart,"depart":depart,'branch_lst':branch_lst,'designation_lst':designation_lst})

    elif request.method == "POST":
        
        data = {
            
            "Employee_Name": request.POST.get("employee_name"),
            "Gender":  request.POST.get("gender"),
            "Date_Of_Birth": request.POST.get("dob"),
            "Blood_Group": request.POST.get("blood"),
            "Date_Of_Joining": request.POST.get("doj"),
            "Phone_Number": request.POST.get("phone"),
            "Email_Id": request.POST.get("email"),
            "Department": request.POST.get("department"),
            "Designation": request.POST.get("designation"),
            "Qualification": request.POST.get("qualification"),
            "Current_Address":request.POST.get("cur_address"),
            "Permanent_Address":request.POST.get("Per_address"),
            "Aadhar_Number": request.POST.get("aadhar"),
            "Pan_Number": request.POST.get("pan"),
            "EPF_Number":request.POST.get("EPF"),
            
            "Previous_Experience": request.POST.get("experience"), 
            "Experience_years" : request.POST.get("experience_years"),
            "Reference_Through"  : request.POST.get("reference_through"),
            "Previous_Company_Name"  : request.POST.get("previous_Company_name"),
            "Referece_Name" : request.POST.get("reference_name"),
            "Branch"  : request.POST.get("branch"),
            
            "Bank_Name" : request.POST.get("bank_name"),
            "Account_Number": request.POST.get("account_number"),
            "Account_Holder_Name": request.POST.get("account_holder_name"),
            "IFSC_Code": request.POST.get("ifsc"),
            "Branch_Name" : request.POST.get("branch_name"),
            
            "Salary_Type": request.POST.get("salary_type"),
            "Basic_Pay" : request.POST.get("basic_pay"),
            "Working_Hours" : request.POST.get("working_hours"),
            "Casual_Leave_Permonth" : request.POST.get("casual_leave_per_month"),
            "HRA" : request.POST.get("hra"),
            "Medical_Allowence" : request.POST.get("medical_allowence"),
            "Conveyance_Allowence": request.POST.get("conveyance_allowence"),
            "General_Allowence": request.POST.get("general_allowence"),
            "Professional_Tax": request.POST.get("professional_tax"),
            "RD" : request.POST.get("rd"),
            "PF" : request.POST.get("pf"),
            "ESI" : request.POST.get("esi"),
            "Net_Salary" : request.POST.get("net_salary")
                    
        }
        #print(data)
        ids = {'id': employee_id}
        #print(ids)
        put_response = requests.put(put_url, params=ids, json=data)
        #print(put_response)
        if put_response.status_code == 200:
            return redirect("employee_list") 
        return render(request, "Master/employee_list.html") 
    
#employee_list
def Employee_filter(request):
     
    departments = request.POST.get('department')
    url = 'http://127.0.0.1:8000/employee/department_filter/'
    params = {
        'departments': departments,
        
    }
    print(departments)

    response = requests.get(url, params=params)
    if response.status_code == 200:
        #print(response.json())
        return JsonResponse(response.json(), safe=False)
    
    else:
        print('Error:', response.status_code)
        return JsonResponse(response, safe=False)
    



