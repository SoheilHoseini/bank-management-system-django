from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_employees/', AllEmployees),
    path('all_branches/', AllBranches),
    path('all_customers/', AllCustomers),
    path('all_transactions/', AllTrans),
    path('all_deposits/', AllDeposits),
    path('get_transaction/', GetTransaction),
    path('get_customer/', GetCustomer),
    path('get_employee/', GetEmployee),
    path('signup/', signup),
    path('login/', login),
    path('change_password/', change_password),
    path('logout/', logout),
]
