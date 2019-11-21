from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    contact_no=models.CharField(max_length=10)


class EmployeeDetail(models.Model):
    empname=models.CharField(max_length=20)
    empno=models.CharField(max_length=12)
    empsal=models.CharField(max_length=15)
    eemail=models.EmailField(max_length=70, null=True, blank=True, unique=True)


class BankDetail(models.Model):
    bankname=models.CharField(max_length=20)
    address=models.CharField(max_length=16)
    ifsc=models.CharField(max_length=7)
    bemail=models.EmailField(max_length=70, null=True, blank=True, unique=True)
class EmpBankdetails(models.Model):
    name=models.ForeignKey(EmployeeDetail,on_delete=models.CASCADE)
    bname=models.ForeignKey(BankDetail,on_delete=models.CASCADE)
    accountno=models.CharField(max_length=16)

# class resmodel(models.Model):
#     resume_header = models.CharField(max_length=100)
#     upload_resume = models.FileField(upload_to='documents')



