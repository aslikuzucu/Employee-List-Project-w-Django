
from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee

def home(request):
    employess = Employee.objects.all()
    context = {
        'employees': employess,
    }
    return render(request, 'home.html', context)