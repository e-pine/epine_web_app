# Generated by Django 4.2.7 on 2024-01-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0047_event_status'),
        ('chat', '0016_delete_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pine.category'),
        ),
    ]
