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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    father_name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    cellphone_number = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=8, unique=True)
    education = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=15, choices=MARITAL_CHOICES)
    nationality = models.CharField(max_length=20)


class Deposit(models.Model):
    pass


class Contract(models.Model):
    pass


class Branch(models.Model):
    b_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=45, null=True)
    chief_name = models.CharField(max_length=45, null=True)
    address = models.TextField(max_length=200, null=True)


class Employee(models.Model):
    employment_date = models.DateField()
    email = models.EmailField()
    employment_status = models.CharField(max_length=45)
    job_position = models.CharField(max_length=45)
    e_dp_id = models.ForeignKey(Deposit)
    e_national_id = models.ForeignKey(PersonalInformation, to_field='national_id')
    e_contract_id = models.ForeignKey(Contract)
    e_b_id = models.ForeignKey(Branch, to_field='b_id')


class Customer(models.Model):
    c_id = models.IntegerField()


class Loan(models.Model):
    pass


class Securities(models.Model):
    pass


class Card(models.Model):
    pass


class Check(models.Model):
    pass


class Transaction(models.Model):
    pass


