from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from tastypie.exceptions import BadRequest
from django.views import generic
import requests
from .models import Department
from django.http import JsonResponse

api_url = "http://127.0.0.1:8000/polls/api/v1"

class EmployeeSuccessView(generic.ListView):
    template_name = "polls/employee_success.html"
    def get_queryset(self):
        return ''
    
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    def get_queryset(self):
        return ''

class EmployeeView(generic.ListView):
    template_name = "polls/list_employees.html"
    def get_queryset(self):
        return ''

def signup(request):
    if request.method == "POST":
        # Collect data from the submitted form
        name = request.POST.get("name")
        salary = request.POST.get("salary")
        department_id = request.POST.get("department")  # Assume department is selected by ID
        position = request.POST.get("position")
        date_of_birth = request.POST.get("date_of_birth")
        
        # Payload to send to the API
        data = {
            "date_of_birth": date_of_birth,
            "department": f'/polls/api/v1/department/{department_id}/',
            "name": name,
            "position": position,
            "resource_uri": "",
            "salary": int(salary)
        }

        headers = {
            "Content-Type": "application/json",
            # Include authentication header if required
            # "Authorization": "ApiKey username:apikey"
        }

        try:
            # Send data to the API
            response = requests.post(f'{api_url}/employee/', json=data, headers=headers)
            # Check API response
            if response.status_code in [200, 201]:
                # return JsonResponse({"message": "Employee created successfully!"}, status=201)
                return redirect("employee_success")  # Redirect on success
            else:
                return render(
                    request,
                    "polls/signup.html",
                    {
                        "error": "Failed to create employee. Please try again.",
                        "status_code": response.status_code,
                        "response_text": response.text,
                    },
                )
        except requests.exceptions.RequestException as e:
            return render(
                request,
                "polls/signup.html",
                {"error": f"API connection error: {str(e)}", "status_code": 500},
            )
    # For GET requests, fetch all departments for the dropdown
    context =   {'departments' : Department.objects.all()}
    return render(request, "polls/signup.html", context)

def list_employees(request):
    try:
        # Send GET request to the API
        response = requests.get(api_url + 'employee')
        
        # Check response status
        if response.status_code == 200:
            employees = response.json().get("objects", [])  # Tastypie typically returns "objects" key
        else:
            employees = []
            error = f"Error {response.status_code}: {response.text}"
            return render(request, "list_employees.html", {"employees": employees, "error": error})

    except requests.exceptions.RequestException as e:
        employees = []
        error = str(e)
        return render(request, "list_employees.html", {"employees": employees, "error": error})

    # Render the template with the list of employees
    return render(request, "list_employees.html", {"employees": employees})