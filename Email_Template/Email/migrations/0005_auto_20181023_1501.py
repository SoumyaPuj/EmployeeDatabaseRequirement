# Generated by Django 2.1.2 on 2018-10-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0004_auto_20181023_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_design',
            name='EXPIRY_DATE',
            field=models.DateField(max_length=15),
        ),
        migrations.AlterField(
            model_name='email_design',
            name='ISSUED_DATE',
            field=models.DateField(max_length=15),
        ),
    ]
