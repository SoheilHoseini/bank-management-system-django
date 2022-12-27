from django.db import models


# Create your models here.
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
    education = models.CharField(max_length=10)
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
    branch_id = models.ForeignKey(Branch, to_field='b_id')


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
    e_dp_id = models.ForeignKey(Deposit, to_field='d_num')
    e_national_id = models.ForeignKey(PersonalInformation, to_field='national_id')
    e_contract_id = models.ForeignKey(Contract)
    e_b_id = models.ForeignKey(Branch, to_field='b_id')


class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True, unique=True)
    c_national_id = models.ForeignKey(PersonalInformation, to_field='national_id')
    c_contract_id = models.ForeignKey(Contract)
    c_dp_num = models.ForeignKey(Deposit, to_field='d_num')


class Loan(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=45)
    interest_rate = models.FloatField()
    number_of_debts = models.IntegerField()
    guarantor_job = models.CharField(max_length=45)
    guarantor_cnt = models.IntegerField()
    l_customer_id = models.ForeignKey(Customer, to_field='c_id')


class Securities(models.Model):
    security_id = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=45)
    value = models.FloatField()
    purchase_date = models.DateField()
    expire_date = models.DateField()
    s_cust_id = models.ForeignKey(Customer, to_field='c_id')


class Card(models.Model):
    card_num = models.IntegerField(primary_key=True, unique=True, max_length=16)
    expire_date = models.DateField()
    cvv2 = models.IntegerField(unique=True)
    card_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10)


class Check(models.Model):
    serial_num = models.IntegerField(primary_key=True, unique=True)
    ch_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10)


class Transaction(models.Model):
    amount = models.FloatField()
    receiver_first_name = models.CharField(max_length=45)
    receiver_last_name = models.CharField(max_length=45)
    source_bank = models.CharField(max_length=45)
    destination_bank = models.CharField(max_length=45)
    destination_deposit_num = models.CharField(max_length=45)
    tr_dp_num = models.ForeignKey(Deposit, to_field='d_num', max_length=10)

