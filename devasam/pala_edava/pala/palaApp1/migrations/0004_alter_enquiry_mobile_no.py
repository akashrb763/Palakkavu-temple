# Generated by Django 4.2 on 2023-05-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palaApp1', '0003_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='mobile_no',
            field=models.TextField(),
        ),
    ]
