# Generated by Django 4.0.4 on 2022-05-15 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0006_employmentdetails_staff_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentdetails',
            name='staff_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registry.staffcategory'),
        ),
    ]
