# Generated by Django 5.0.7 on 2024-08-02 12:28

import django.core.validators
import ravi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hlbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[ravi.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='plbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[ravi.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='basicdetailform',
        ),
    ]
