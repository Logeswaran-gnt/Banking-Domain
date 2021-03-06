# Generated by Django 2.2.4 on 2020-05-02 10:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('personalbanking', '0001_initial'), ('personalbanking', '0002_auto_20200502_1031')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(default='Chennai', max_length=30)),
                ('address', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.IntegerField()),
                ('loan_types', models.CharField(choices=[('PL', 'Personal Loan'), ('HL', 'Housing Loan'), ('VL', 'Vehicle Loan')], default='PL', max_length=2)),
                ('interest_rate', models.FloatField()),
                ('total_loan', models.FloatField()),
                ('pending_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('account_number', models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('account_type', models.CharField(choices=[('SB', 'Savings Account'), ('CA', 'Current Account')], default='SB', max_length=2)),
                ('created_time', models.DateField(auto_now_add=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbanking.Branch')),
                ('loan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personalbanking.Loan')),
            ],
        ),
    ]
