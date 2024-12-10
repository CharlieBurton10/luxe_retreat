# Generated by Django 3.2.25 on 2024-12-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='treatment',
            name='preferred_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]