from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .render import *


def ShowEmployees(request):
    return HttpResponse("List of all employees:")


def ShowBranches(request):
    all_branches = Branch.objects.all().values_list('name', 'chief_name', 'address')
    readable = render_to_readable_output(all_branches)
    return HttpResponse(readable)

