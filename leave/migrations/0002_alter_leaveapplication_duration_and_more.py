# Generated by Django 4.0.3 on 2022-03-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='requested_duration',
            field=models.IntegerField(),
        ),
    ]
