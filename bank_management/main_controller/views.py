from django.shortcuts import render
from django.http import HttpResponse


def ShowEmployees(request):
    return HttpResponse("List of all employees:")

