# Generated by Django 4.1.7 on 2023-02-24 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_phtgobooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phtgobooking',
            name='bdate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='phtgobooking',
            name='cardno',
            field=models.CharField(default='0', max_length=15),
        ),
        migrations.AlterField(
            model_name='phtgobooking',
            name='serv',
            field=models.CharField(max_length=40),
        ),
    ]