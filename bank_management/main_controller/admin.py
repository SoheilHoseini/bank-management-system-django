from django.contrib import admin
from .models import *


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Securities)
class SecuritiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

