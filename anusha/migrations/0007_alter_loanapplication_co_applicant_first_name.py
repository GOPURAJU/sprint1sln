# Generated by Django 5.0.6 on 2024-08-08 12:42

import anusha.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anusha', '0006_alter_basicdetailform_required_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='co_applicant_first_name',
            field=models.CharField(default='a', max_length=50, validators=[anusha.models.validate_only_letters]),
        ),
    ]
