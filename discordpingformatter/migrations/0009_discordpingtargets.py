# Generated by Django 2.2.15 on 2020-09-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("discordpingformatter", "0008_auto_20200911_1802"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscordPingTargets",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the Discord role to ping",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "discord_id",
                    models.CharField(
                        help_text="ID of the Discord role to ping",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        default=None,
                        help_text="You can add notes about this configuration here if you want",
                        null=True,
                    ),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Whether this formup location is enabled or not",
                    ),
                ),
                (
                    "restricted_to_group",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Restrict the right to ping this Discord group to one or more groups.",
                        related_name="discord_role_require_groups",
                        to="auth.Group",
                    ),
                ),
            ],
            options={
                "verbose_name": "Discord Ping Target",
                "verbose_name_plural": "Discord Ping Targets",
                "default_permissions": (),
            },
        ),
    ]
