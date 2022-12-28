from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .render import *


def AllEmployees(request):
    all_employees = Employee.objects.select_related('e_national_id').values_list('e_national_id__first_name',
                                                                                 'e_national_id__last_name',
                                                                                 'job_position',
                                                                                 'e_national_id',
                                                                                 'e_national_id__employee__employment_status')
    readable = render_to_readable_output(all_employees)
    return HttpResponse(readable)


def AllBranches(request):
    all_branches = Branch.objects.all().values_list('name', 'chief_name', 'address')
    readable = render_to_readable_output(all_branches)
    return HttpResponse(readable)


def AllCustomers(request):
    all_customers = Customer.objects.select_related('c_national_id').values_list('c_national_id__first_name',
                                                                                 'c_national_id__last_name',
                                                                                 'c_national_id',
                                                                                 'c_national_id__customer__c_dp_num')
    readable = render_to_readable_output(all_customers)
    return HttpResponse(readable)


def AllDeposits(request):
    all_deposits = Deposit.objects.all()


def AllTrans(request):
    all_trans = Transaction.objects.all()