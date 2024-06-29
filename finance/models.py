from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import transaction as db_transaction 

class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(email, user_name, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,default='example@example.com')
    user_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return f"{self.user_name} ({self.email})"

class Profile(models.Model):
  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_register = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name + ' ' + self.last_name

class Account_type(models.Model):
  ID_account_type = models.AutoField(primary_key=True)
  description = models.CharField(max_length=50)

  def __str__(self):
    return self.description

class Currency(models.Model):
  ID_currency = models.AutoField(primary_key=True)
  description = models.CharField(max_length=50)
  symbol = models.CharField(max_length=5)

  def __str__(self):
    return self.description

class Account(models.Model):
  ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
  ID_Type = models.ForeignKey(Account_type, on_delete=models.CASCADE)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  ID_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
  Institution = models.CharField(max_length=50)
  holder = models.CharField(max_length=50, default='holder')
  number = models.CharField(max_length=50, default='0000000000000000')
  expiry = models.CharField(max_length=50, default='2025-12-31')
  type = models.CharField(max_length=50, default='visa')

  def __str__(self):
    return self.Institution

class Fiance_goal(models.Model):
    ID_goal = models.AutoField(primary_key=True)
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    achieved = models.BooleanField(default=False)
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class Finance_tip(models.Model):
  ID_tip = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200)
  Date_plubication = models.DateField()

  def __str__(self):
    return self.description


class Acces_tip(models.Model):
  ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
  ID_tip = models.ForeignKey(Finance_tip, on_delete=models.CASCADE)
  date = models.DateField()


class Transaction(models.Model):
  ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
  ID_account = models.ForeignKey(Account, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField(auto_now_add=True)
  description = models.CharField(max_length=200)
  type = models.ForeignKey('Type_transaction', on_delete=models.CASCADE)

  def __str__(self):
      return self.description


class Type_transaction(models.Model):
  ID_type = models.AutoField(primary_key=True)
  description = models.CharField(max_length=50)

  def __str__(self):
    return self.description