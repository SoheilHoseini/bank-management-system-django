from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100)


class PersonalInformation(models.Model):
    GENDER_CHOICES = (
        ("m", "male"),
        ("f", "female"),
    )

    MARITAL_CHOICES = (
        ('m', 'married'),
        ('s', 'single'),
    )

    national_id = models.CharField(max_length=10, primary_key=True, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthdate = models.DateField()
    father_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField(max_length=200)
    cellphone_number = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=8, unique=True)
    education = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    nationality = models.CharField(max_length=10)


class Branch(models.Model):
    b_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=45)
    chief_name = models.CharField(max_length=45)
    address = models.TextField(max_length=200)


class Deposit(models.Model):
    d_num = models.CharField(max_length=10, primary_key=True, unique=True)
    start_date = models.DateField()
    deposit_type = models.CharField(max_length=45)
    interest_rate = models.FloatField()
    amount = models.FloatField()
    branch_id = models.ForeignKey(Branch, to_field='b_id', on_delete=models.CASCADE)


class Contract(models.Model):
    start_date = models.DateField()
    expire_date = models.DateField()
    type = models.CharField(max_length=45)
    second_side_national_id = models.CharField(max_length=10, unique=True)


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, unique=True)
    employment_date = models.DateField()
    email = models.EmailField()
    employment_status = models.CharField(max_length=45)
    job_position = models.CharField(max_length=45)
    e_dp_id = models.ForeignKey(Deposit, to_field='d_num', on_delete=models.CASCADE)
    e_national_id = models.ForeignKey(PersonalInformation, to_field='national_id', on_delete=models.CASCADE)
    e_contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    e_b_id = models.ForeignKey(Branch, to_field='b_id', on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)


class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True, unique=True)
    c_national_id = models.ForeignKey(PersonalInformation, to_field='national_id', on_delete=models.CASCADE)
    c_contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    c_dp_num = models.ForeignKey(Deposit, to_field='d_num', on_delete=models.CASCADE)


class Loan(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=45)
    interest_rate = models.FloatField()
    number_of_debts = models.IntegerField()
    guarantor_job = models.CharField(max_length=45)
    guarantor_cnt = models.IntegerField()
    l_customer_id = models.ForeignKey(Customer, to_field='c_id', on_delete=models.CASCADE)


class Securities(models.Model):
    security_id = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=45)
    value = models.FloatField()
    purchase_date = models.DateField()
    expire_date = models.DateField()
    s_cust_id = models.ForeignKey(Customer, to_field='c_id', on_delete=models.CASCADE)


class Card(models.Model):
    card_num = models.IntegerField(primary_key=True, unique=True)
    expire_date = models.DateField()
    cvv2 = models.IntegerField(unique=True)
    card_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10, on_delete=models.CASCADE)


class Check(models.Model):
    serial_num = models.IntegerField(primary_key=True, unique=True)
    ch_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10, on_delete=models.CASCADE)


class Transaction(models.Model):
    amount = models.FloatField()
    receiver_first_name = models.CharField(max_length=45)
    receiver_last_name = models.CharField(max_length=45)
    source_bank = models.CharField(max_length=45)
    destination_bank = models.CharField(max_length=45)
    destination_deposit_num = models.CharField(max_length=45)
    tr_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10, on_delete=models.CASCADE)

