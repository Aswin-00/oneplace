# Generated by Django 4.1.7 on 2023-02-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_opric_phtgo_opric'),
    ]

    operations = [
        migrations.AddField(
            model_name='usinf',
            name='prv',
            field=models.CharField(default='USR', max_length=3),
        ),
    ]
