# Generated by Django 2.2 on 2020-12-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0006_auto_20201207_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
