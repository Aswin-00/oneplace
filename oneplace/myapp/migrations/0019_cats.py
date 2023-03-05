# Generated by Django 4.1.7 on 2023-02-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_cabobooking_rtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='CATS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pckname', models.CharField(max_length=40)),
                ('foodit', models.CharField(max_length=200)),
                ('bkch', models.IntegerField()),
                ('pech', models.IntegerField()),
                ('cimg', models.ImageField(upload_to='CATS/images/')),
            ],
        ),
    ]
