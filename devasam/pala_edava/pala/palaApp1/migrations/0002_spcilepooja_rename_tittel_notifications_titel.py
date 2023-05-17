# Generated by Django 4.1.5 on 2023-04-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palaApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='spcilepooja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pooja_name', models.CharField(max_length=80)),
                ('sponser', models.CharField(max_length=100)),
                ('sponser_addres', models.CharField(max_length=300)),
                ('pooja_time', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='notifications',
            old_name='tittel',
            new_name='titel',
        ),
    ]