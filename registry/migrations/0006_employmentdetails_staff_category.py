# Generated by Django 4.0.3 on 2022-05-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_staffcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmentdetails',
            name='staff_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registry.staffcategory'),
            preserve_default=False,
        ),
    ]