# Generated by Django 4.1.7 on 2023-02-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spd',
            name='pnum',
            field=models.IntegerField(),
        ),
    ]
