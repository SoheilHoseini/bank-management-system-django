from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .render import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f"{form.errors}")

    return HttpResponse('Only post method allowed!')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponse('Login completed!')
        return HttpResponse('Wrong password/username')

    return HttpResponse('Please login with post method')


@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')

        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password')

        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical')

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('Password changed successfully!')

    return HttpResponse('Only post method allowed')


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')

        dj_logout(request)
        return HttpResponse('Logout successfully')

    return HttpResponse('Only post method allowed')


def AllEmployees(request):
    all_employees = Employee.objects.select_related('e_national_id').values('e_national_id__first_name',
                                                                            'e_national_id__last_name',
                                                                            'job_position',
                                                                            'e_national_id',
                                                                            'e_national_id__employee__employment_status')
    return JsonResponse(list(all_employees), safe=False)


def AllBranches(request):
    all_branches = Branch.objects.all().values('name', 'chief_name', 'address')
    return JsonResponse(list(all_branches), safe=False)


def AllCustomers(request):
    all_customers = Customer.objects.select_related('c_national_id').values('c_national_id__first_name',
                                                                            'c_national_id__last_name',
                                                                            'c_national_id',
                                                                            'c_national_id__customer__c_dp_num')
    readable = render_to_readable_output(all_customers)
    return JsonResponse(list(all_customers), safe=False)


def AllDeposits(request):
    all_deposits = Customer.objects.select_related('c_dp_num').values('c_national_id__first_name',
                                                                      'c_national_id__last_name',
                                                                      'c_dp_num',
                                                                      'c_dp_num__deposit_type')
    return JsonResponse(list(all_deposits), safe=False)


def AllTrans(request):
    all_trans = Transaction.objects.select_related('tr_dp_num').values('source_bank',
                                                                       'amount',
                                                                       'destination_bank',
                                                                       'destination_deposit_num')
    return JsonResponse(list(all_trans), safe=False)


@csrf_exempt
def GetTransaction(request):
    trans_id = request.POST.get('trans_id')
    try:
        trans = Transaction.objects.get(id=trans_id)
        return JsonResponse({"amount": trans.amount, "source_bank": trans.source_bank,
                             "destination_bank": trans.destination_bank, "tr_dp_num": trans.tr_dp_num.d_num})
        # return HttpResponse(f"{trans.amount, trans.source_bank, trans.destination_bank,trans.tr_dp_num.d_num}")
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
        return JsonResponse({"first_name": customer.c_national_id.first_name,
                             "last_name": customer.c_national_id.last_name,
                             "national_id": customer.c_national_id.national_id,
                             "cellphone_number": customer.c_national_id.cellphone_number,
                             "c_dp_num": customer.c_dp_num.d_num})

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
        return JsonResponse({"first_name": employee.e_national_id.first_name,
                             "last_name": employee.e_national_id.last_name,
                             "national_id": employee.e_national_id.national_id,
                             "cellphone_number": employee.e_national_id.cellphone_number,
                             "education": employee.e_national_id.education,
                             "salary": employee.salary,
                             "job_position": employee.job_position,
                             "employment_date": employee.employment_date})
    except Employee.DoesNotExist:
        return HttpResponse(
            f"<p>"
            f"<b>۴۰۴</b>"
            f"</p>"
            f"این کارمند وجود ندارد."
        )
