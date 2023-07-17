from django.shortcuts import render
import requests

def Dashboard(request):
    emp_lst = 'http://127.0.0.1:8000/employee_get/'
    get_response = requests.get(emp_lst)
    Emp = get_response.json()
    count = len(Emp)
    #print("+++++++++++++++++",count)
    return render(request,"Dashboard/Dashboard.html",{"count":count,'Emp':Emp})










