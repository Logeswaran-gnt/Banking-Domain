# Generated by Django 2.2.4 on 2020-05-04 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalbanking', '0001_squashed_0002_auto_20200502_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personalbanking.Loan'),
        ),
    ]
