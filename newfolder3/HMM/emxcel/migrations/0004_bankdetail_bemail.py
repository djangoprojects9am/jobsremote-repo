# Generated by Django 2.2.3 on 2019-09-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emxcel', '0003_employeedetail_eemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetail',
            name='bemail',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
