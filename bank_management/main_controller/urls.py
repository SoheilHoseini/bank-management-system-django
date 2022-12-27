from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_employees/', ShowEmployees),
    path('all_branches/', ShowBranches),
]
