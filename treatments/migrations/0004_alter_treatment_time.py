# Generated by Django 3.2.25 on 2025-01-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0003_remove_treatment_preferred_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
