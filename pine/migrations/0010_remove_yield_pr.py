# Generated by Django 4.2.4 on 2023-10-07 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0009_yield_pr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yield',
            name='pr',
        ),
    ]
