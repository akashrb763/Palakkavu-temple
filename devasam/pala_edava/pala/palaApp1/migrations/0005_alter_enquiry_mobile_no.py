# Generated by Django 4.2 on 2023-05-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palaApp1', '0004_alter_enquiry_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='mobile_no',
            field=models.TextField(blank=True, null=True),
        ),
    ]
