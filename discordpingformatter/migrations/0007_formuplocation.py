# Generated by Django 2.2.15 on 2020-09-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordpingformatter', '0006_fleetdoctrine'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormupLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Short name to identify this formup location', max_length=64, unique=True)),
                ('notes', models.TextField(blank=True, default=None, help_text='You can add notes about this formup location here if you want', null=True)),
                ('is_enabled', models.BooleanField(db_index=True, default=True, help_text='Whether this formup location is enabled or not')),
            ],
            options={
                'verbose_name': 'Formup Location',
                'verbose_name_plural': 'Formup Locations',
                'default_permissions': (),
            },
        ),
    ]