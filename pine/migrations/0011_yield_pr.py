# Generated by Django 4.2.4 on 2023-10-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0010_remove_yield_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='yield',
            name='pr',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
