from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_employees/', AllEmployees),
    path('all_branches/', AllBranches),
    path('all_customers/', AllCustomers),
    path('all_transactions/', AllTrans),
    path('all_deposits', AllDeposits),
]
