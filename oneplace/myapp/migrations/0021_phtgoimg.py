# Generated by Django 4.1.7 on 2023-03-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_catsbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='PHTGOimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('img', models.ImageField(upload_to='PHTGO/useraddimg/')),
            ],
        ),
    ]
