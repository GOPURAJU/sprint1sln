# Generated by Django 5.0.6 on 2024-08-06 07:57

import ravi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0003_alter_customerprofile_coapplicant_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='coapplicant_age',
            field=models.IntegerField(default='', validators=[ravi.models.validate_age]),
        ),
    ]
