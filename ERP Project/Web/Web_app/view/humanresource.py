from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
from django.contrib import messages
import datetime

def Human_resource(request):
    return render(request, "HumanResource/human_resource.html")

#Attendance
def Attendance(request):
    url = 'http://127.0.0.1:8000'
    emp_lst = f'{url}/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
    branch = 'http://127.0.0.1:8000/branch_get/'
    get_response = requests.get(branch)
    branch_lst = get_response.json()
    
    if request.method == 'POST':
        data = {
            'Date' : request.POST.get("date"),
            'Employee_Name': request.POST.get("employee_name"),
            'Working_Hours': request.POST.get("working_hours"),
            'Worked_Hours': request.POST.get("worked_hours"),
            'Over_Time': request.POST.get("over_time"),
            'Permission': request.POST.get("permission"),
            'Casual_Leave': request.POST.get("cl"),    
            'Sick_Leave': request.POST.get("sl"),
            'Status': request.POST.get("status"),
                         
        }
        response = requests.post(f'{url}/attendance/', data=data)
        if response.status_code == 201 or response.status_code == 200:
            messages.success(request, "Attendance Posted Successfully")
            print(response.json())
            return JsonResponse(response.json(), safe=False)
        else:
            print(data)
            print("++++++++ error")
            messages.error(request, "Attendance Posted Error..!")
            return redirect('attendance')
    else:
        return render(request, "HumanResource/attendance.html",{'emp_lst':Emp,'branch_lst':branch_lst})

def Datewise_Atendance(request):
    messages.success(request, 'Employee Created Succesfull.')
    dates = request.POST.get('date')
    url = 'http://127.0.0.1:8000/datewise_attendance/'
    params = {
        'date': dates,
    }
    print(dates)

    response = requests.get(url, params=params)
    if response.status_code == 200:
        #print(response.json())
        return JsonResponse(response.json(), safe=False)
    
    else:
        print('Error:', response.status_code)
        return JsonResponse(response, safe=False)

#Attendance_List
def Attendance_List(request):
    attendance = 'http://127.0.0.1:8000/attendance/get/'
    get_response = requests.get(attendance)
    attendance_lst = get_response.json()
    
    url = 'http://127.0.0.1:8000'
    emp_lst = f'{url}/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
    
    branch = 'http://127.0.0.1:8000/branch_get/'
    get_response = requests.get(branch)
    branch_lst = get_response.json()
    
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month

    # Get the first and last day of the current month
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, 1) + datetime.timedelta(days=32)
    last_day = last_day.replace(day=1) - datetime.timedelta(days=1)

    # Generate a list of dates for the current month
    dates = [first_day + datetime.timedelta(days=x) for x in range((last_day - first_day).days + 1)]

    return render(request, "HumanResource/attendance_list.html",{'attendance_lst':attendance_lst,'current_date':current_date,'Emp':Emp,'branch_lst':branch_lst,'dates': dates})

def Monthwise_Atendance(request):
    
    Month_Year = request.POST.get('month_year')
    print(Month_Year)    
    url = 'http://127.0.0.1:8000/monthwise_attendance/'
    params = {
        'month_year': Month_Year,
    }
  
    response = requests.get(url, params=params)
    if response.status_code == 200:
        datas=response.json()
        """datas1= datas['Attendance']
        print('-----------',datas1[0])"""
        return JsonResponse(response.json(), safe=False)
    
    else:
        print('Error:', response.status_code)
        return JsonResponse(response, safe=False)
