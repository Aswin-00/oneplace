# Generated by Django 4.1.7 on 2023-02-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_phtog_usinf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usinf',
            old_name='userpW',
            new_name='userpw',
        ),
    ]
