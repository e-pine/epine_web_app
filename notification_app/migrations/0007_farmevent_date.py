# Generated by Django 4.2.7 on 2024-01-18 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0006_broadcastnotification_variety'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmevent',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
