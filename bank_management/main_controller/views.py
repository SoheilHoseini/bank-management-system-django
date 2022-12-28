from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .render import *

from django.views.decorators.csrf import csrf_exempt


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
    all_deposits = Customer.objects.select_related('c_dp_num').values_list('c_national_id__first_name',
                                                                           'c_national_id__last_name',
                                                                           'c_dp_num',
                                                                           'c_dp_num__deposit_type')
    readable = render_to_readable_output(all_deposits)
    return HttpResponse(readable)


def AllTrans(request):
    all_trans = Transaction.objects.select_related('tr_dp_num').values_list('source_bank',
                                                                            'amount',
                                                                            'destination_bank',
                                                                            'destination_deposit_num')
    readable = render_to_readable_output(all_trans)
    return HttpResponse(readable)


@csrf_exempt
def GetTransaction(request):
    trans_id = request.POST.get('trans_id')
    try:
        trans = Transaction.objects.get(id=trans_id)
        return HttpResponse(f"{trans.amount, trans.source_bank, trans.destination_bank,trans.tr_dp_num.d_num}")
    except Transaction.DoesNotExist:
        return HttpResponse(
            f"<p>"
            f"<b>۴۰۴</b>"
            f"</p>"
            f"چنین تراکنشی وجود ندارد."
        )


@csrf_exempt
def GetCustomer(request):
    c_national_id = request.POST.get('c_national_id')
    try:
        customer = Customer.objects.get(c_national_id=c_national_id)
        return HttpResponse(f"{customer.c_national_id.first_name}"
                            f", {customer.c_national_id.last_name}"
                            f", {customer.c_national_id.national_id}"
                            f", {customer.c_national_id.cellphone_number}"
                            f", {customer.c_dp_num}")
    except Customer.DoesNotExist:
        return HttpResponse(
            f"<p>"
            f"<b>۴۰۴</b>"
            f"</p>"
            f"این مشتری وجود ندارد."
        )


@csrf_exempt
def GetEmployee(request):
    e_national_id = request.POST.get('e_national_id')
    try:
        employee = Employee.objects.get(e_national_id=e_national_id)
        return HttpResponse(f"{employee.e_national_id.first_name}"
                            f", {employee.e_national_id.last_name}"
                            f", {employee.e_national_id.national_id}"
                            f", {employee.e_national_id.cellphone_number}"
                            f", {employee.e_national_id.education}"
                            f", {employee.salary}"
                            f", {employee.job_position}"
                            f", {employee.employment_date}")
    except Employee.DoesNotExist:
        return HttpResponse(
            f"<p>"
            f"<b>۴۰۴</b>"
            f"</p>"
            f"این کارمند وجود ندارد."
        )
