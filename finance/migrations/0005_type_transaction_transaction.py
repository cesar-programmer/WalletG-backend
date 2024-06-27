# Generated by Django 5.0.6 on 2024-06-26 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_fiance_goal_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_transaction',
            fields=[
                ('ID_type', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('ID_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.account')),
                ('ID_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.type_transaction')),
            ],
        ),
    ]
