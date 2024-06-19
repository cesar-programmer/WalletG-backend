from django.db import models

class user(models.Model):
  user_name = models.CharField(max_length=50)
  user_email = models.EmailField(max_length=50)
  user_password = models.CharField(max_length=50)

  def __str__(self):
    return self.user_name + ' ' + self.user_email

class profile(models.Model):
  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_register = models.DateField()
  user = models.ForeignKey(user, on_delete=models.CASCADE)

  def __str__(self):
    return self.name + ' ' + self.last_name

class account_type(models.Model):
  ID_account_type = models.AutoField(primary_key=True)
  description = models.CharField(max_length=50)

  def __str__(self):
    return self.description

class currency(models.Model):
  ID_currency = models.AutoField(primary_key=True)
  description = models.CharField(max_length=50)
  symbol = models.CharField(max_length=5)

  def __str__(self):
    return self.description

class account(models.Model):
  ID_user = models.ForeignKey(user, on_delete=models.CASCADE)
  ID_Type = models.ForeignKey(account_type, on_delete=models.CASCADE)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  ID_currency = models.ForeignKey(currency, on_delete=models.CASCADE)
  Institution = models.CharField(max_length=50)
  holder = models.CharField(max_length=50, default='holder')
  number = models.CharField(max_length=50, default='0000000000000000')
  expiry = models.CharField(max_length=50, default='2025-12-31')
  type = models.CharField(max_length=50, default='visa')

  def __str__(self):
    return self.Institution

class fiance_goal(models.Model):
  ID_goal = models.AutoField(primary_key=True)
  ID_user = models.ForeignKey(user, on_delete=models.CASCADE)
  description = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField()
  achieved = models.BooleanField()


class finance_tip(models.Model):
  ID_tip = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200)
  Date_plubication = models.DateField()

  def __str__(self):
    return self.description


class acces_tip(models.Model):
  ID_user = models.ForeignKey(user, on_delete=models.CASCADE)
  ID_tip = models.ForeignKey(finance_tip, on_delete=models.CASCADE)
  date = models.DateField()