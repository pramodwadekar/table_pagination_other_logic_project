# Generated by Django 4.2.6 on 2023-10-18 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_student_options_rename_contact_student_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Pincode',
        ),
    ]
