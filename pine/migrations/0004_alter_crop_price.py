# Generated by Django 4.2.4 on 2023-10-03 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0003_pineprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pine.pineprice'),
        ),
    ]
