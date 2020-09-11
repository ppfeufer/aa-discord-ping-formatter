# Generated by Django 2.2.15 on 2020-09-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordpingformatter', '0010_auto_20200911_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='is_embedded',
            field=models.BooleanField(db_index=True, default=True, help_text="Whether this webhook's ping is embedded or not"),
        ),
    ]