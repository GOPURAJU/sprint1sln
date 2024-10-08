# Generated by Django 5.0.7 on 2024-08-02 12:28

import django.core.validators
import django.db.models.deletion
import ganesh.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crebasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[ganesh.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[ganesh.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField(validators=[ganesh.models.validate_date])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.DecimalField(decimal_places=2, max_digits=50, validators=[ganesh.models.validate_amount])),
                ('terms_accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True, validators=[ganesh.models.validate_only_letters])),
                ('date_of_birth', models.DateField(validators=[ganesh.models.validate_date])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=10)),
                ('nationality', models.CharField(max_length=50, null=True, validators=[ganesh.models.validate_only_letters])),
                ('current_street_address', models.CharField(max_length=255, null=True)),
                ('current_city', models.CharField(default='enter', max_length=100, validators=[ganesh.models.validate_only_letters])),
                ('current_state_province', models.CharField(default='Default Value', max_length=100, validators=[ganesh.models.validate_only_letters])),
                ('current_postal_code', models.CharField(blank=True, max_length=6, null=True, validators=[ganesh.models.validate_pincode])),
                ('current_country', models.CharField(blank=True, max_length=50, null=True, validators=[ganesh.models.validate_only_letters])),
                ('permanent_street_address', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_city', models.CharField(blank=True, max_length=100, null=True, validators=[ganesh.models.validate_only_letters])),
                ('permanent_state_province', models.CharField(blank=True, max_length=100, null=True, validators=[ganesh.models.validate_only_letters])),
                ('permanent_postal_code', models.CharField(blank=True, max_length=6, null=True, validators=[ganesh.models.validate_pincode])),
                ('permanent_country', models.CharField(blank=True, max_length=50, null=True, validators=[ganesh.models.validate_only_letters])),
                ('phone_number', models.CharField(max_length=10, null=True, validators=[ganesh.models.validate_mobile_number])),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('employment_status', models.CharField(choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed'), ('Student', 'Student'), ('Retired', 'Retired')], max_length=15, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters])),
                ('employer_name', models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters])),
                ('employer_address', models.CharField(blank=True, max_length=255)),
                ('work_phone_number', models.CharField(max_length=10, null=True, validators=[ganesh.models.validate_mobile_number])),
                ('years_at_current_job', models.PositiveIntegerField(blank=True, null=True)),
                ('monthly_annual_income', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount])),
                ('bank_name', models.CharField(blank=True, max_length=100, validators=[ganesh.models.validate_only_letters])),
                ('account_number', models.CharField(blank=True, max_length=12, null=True, validators=[ganesh.models.validate_accountnumber])),
                ('account_type', models.CharField(blank=True, choices=[('Current', 'Current'), ('Savings', 'Savings')], max_length=10)),
                ('monthly_housing_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount])),
                ('other_monthly_obligations', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount])),
                ('total_monthly_expenses', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[ganesh.models.validate_amount])),
                ('existing_credit_cards', models.IntegerField(blank=True, null=True)),
                ('other_debts_loans', models.IntegerField(blank=True)),
                ('preferred_credit_card_type', models.CharField(blank=True, choices=[('Standard', 'Standard'), ('Rewards', 'Rewards'), ('Travel', 'Travel'), ('Cashback', 'Cashback'), ('Business', 'Business')], max_length=20, validators=[ganesh.models.validate_only_letters])),
                ('purpose_of_credit_card', models.CharField(blank=True, choices=[('Travel', 'Travel'), ('Business', 'Business'), ('Everyday Use', 'Everyday Use'), ('Other', 'Other')], max_length=20, validators=[ganesh.models.validate_only_letters])),
                ('referral_code', models.CharField(blank=True, max_length=50)),
                ('terms_and_conditions_agreed', models.BooleanField(default=False)),
                ('privacy_policy_agreed', models.BooleanField(default=False)),
                ('electronic_signature', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CreditDocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_of_identity', models.FileField(blank=True, help_text='Upload proof of identity such as a passport or driver’s license.', null=True, upload_to='proof_of_identity/', validators=[ganesh.models.validate_pdf_file])),
                ('proof_of_address', models.FileField(blank=True, help_text='Upload proof of address such as a utility bill or lease agreement.', null=True, upload_to='proof_of_address/', validators=[ganesh.models.validate_pdf_file])),
                ('proof_of_income', models.FileField(blank=True, help_text='Upload proof of income such as payslips or tax returns.', null=True, upload_to='proof_of_income/', validators=[ganesh.models.validate_pdf_file])),
                ('personal_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ganesh.creditcardapplication')),
            ],
        ),
    ]
