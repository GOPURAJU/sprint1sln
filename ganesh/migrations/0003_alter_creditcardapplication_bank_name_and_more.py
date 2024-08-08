# Generated by Django 5.0.6 on 2024-08-02 17:22

import ganesh.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganesh', '0002_alter_creditcardapplication_bank_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardapplication',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='current_city',
            field=models.CharField(default='enter', max_length=100, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='current_country',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='current_postal_code',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[ganesh.models.validate_pincode]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='current_state_province',
            field=models.CharField(default='Default Value', max_length=100, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='date_of_birth',
            field=models.DateField(validators=[ganesh.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='employer_name',
            field=models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='full_name',
            field=models.CharField(max_length=100, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='monthly_annual_income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='monthly_housing_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='nationality',
            field=models.CharField(max_length=50, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='other_monthly_obligations',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='permanent_city',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='permanent_country',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='permanent_postal_code',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[ganesh.models.validate_pincode]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='permanent_state_province',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='phone_number',
            field=models.CharField(max_length=10, null=True, validators=[ganesh.models.validate_mobile_number]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='preferred_credit_card_type',
            field=models.CharField(blank=True, choices=[('Standard', 'Standard'), ('Rewards', 'Rewards'), ('Travel', 'Travel'), ('Cashback', 'Cashback'), ('Business', 'Business')], max_length=20, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='purpose_of_credit_card',
            field=models.CharField(blank=True, choices=[('Travel', 'Travel'), ('Business', 'Business'), ('Everyday Use', 'Everyday Use'), ('Other', 'Other')], max_length=20, validators=[ganesh.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='total_monthly_expenses',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount]),
        ),
        migrations.AlterField(
            model_name='creditcardapplication',
            name='work_phone_number',
            field=models.CharField(max_length=10, null=True, validators=[ganesh.models.validate_mobile_number]),
        ),
    ]
