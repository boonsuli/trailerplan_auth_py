# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    civility = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)
    birthday = models.DateField(blank=True, null=True)
    mail = models.CharField(max_length=255)
    city = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32)
    phone = models.CharField(max_length=32, blank=True, null=True)
    user_category = models.CharField(max_length=32, blank=True, null=True)
    role_type = models.CharField(max_length=32, blank=True, null=True)
    login_type = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    encoded_password = models.CharField(max_length=255, blank=True, null=True)
    secret_question = models.CharField(max_length=255, blank=True, null=True)
    encoded_secret_answer = models.CharField(max_length=255, blank=True, null=True)
    encoded_custom_secret_question = models.CharField(max_length=255, blank=True, null=True)
    encoded_custom_secret_answer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
