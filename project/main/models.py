from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Info(models.Model):
#     firstname = models.CharField(max_length=30, db_collation='utf8mb4_unicode_ci')
#     middle_name = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     email = models.CharField(primary_key=True, max_length=50, db_collation='utf8mb4_unicode_ci')
#     password = models.CharField(max_length=50, db_collation='utf8mb4_unicode_ci')
#     acm = models.CharField(max_length=1)
#     acm_id = models.CharField(max_length=50, db_collation='utf8mb4_unicode_ci')
#     paid = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'info'
# Info.objects = Info.objects.using('icmr')

# class Paper(models.Model):
#     email = models.CharField(max_length=50, db_collation='utf8mb4_unicode_ci')
#     paper = models.CharField(primary_key=True, max_length=100, db_collation='utf8mb4_unicode_ci')

#     class Meta:
#         managed = False
#         db_table = 'paper'
# Paper.objects = Paper.objects.using('icmr')

# class Payment(models.Model):
#     email = models.CharField(primary_key=True, max_length=50)
#     num = models.IntegerField()
#     paid = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'payment'
# Payment.objects = Payment.objects.using('icmr')

class MyUser(AbstractUser):
    affiliation = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
# MyUser.objects = MyUser.objects.using('default')