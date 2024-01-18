# Generated by Django 4.2.4 on 2023-10-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0037_workersexpense_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyFerPes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity_used', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
