# Generated by Django 4.0.3 on 2022-05-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveprocess',
            name='date_from',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='date_to',
            field=models.DateField(null=True),
        ),
    ]