# Generated by Django 2.2.15 on 2020-09-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordpingformatter', '0007_formuplocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleetcomm',
            name='name',
            field=models.CharField(help_text='Short name to identify this comms', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='fleetdoctrine',
            name='name',
            field=models.CharField(help_text='Short name to identify this doctrine', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='formuplocation',
            name='name',
            field=models.CharField(help_text='Short name to identify this formup location', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='name',
            field=models.CharField(help_text='Name of the channel this webhook posts to', max_length=255, unique=True),
        ),
    ]
