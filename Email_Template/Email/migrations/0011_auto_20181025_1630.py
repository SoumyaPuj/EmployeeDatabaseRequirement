# Generated by Django 2.1.2 on 2018-10-25 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0010_auto_20181025_1251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email_Design',
            new_name='Email_Information',
        ),
        migrations.AlterModelTable(
            name='email_information',
            table='Email_Information',
        ),
    ]