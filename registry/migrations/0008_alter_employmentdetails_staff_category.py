# Generated by Django 4.0.4 on 2022-05-15 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0007_alter_employmentdetails_staff_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentdetails',
            name='staff_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registry.staffcategory'),
            preserve_default=False,
        ),
    ]