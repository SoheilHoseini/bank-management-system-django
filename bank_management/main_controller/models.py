from django.db import models


# Create your models here.
class PersonalInformation(models.Model):
    national_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    


