# Generated by Django 2.2.15 on 2020-09-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("discordpingformatter", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FleetComm",
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
                        help_text="Short name to identify this comms",
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
                        help_text="Whether this comms is enabled or not",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fleet Comm",
                "verbose_name_plural": "Fleet Comms",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="FleetDoctrine",
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
                        help_text="Short name to identify this doctrine",
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
                        help_text="Whether this doctrine is enabled or not",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fleet Doctrine",
                "verbose_name_plural": "Fleet Doctrines",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="FleetType",
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
                        help_text="Short name to identify this fleet type",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "embed_color",
                    models.CharField(
                        blank=True,
                        help_text="Hightlight color for the embed",
                        max_length=7,
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
                        help_text="Whether this fleet type is enabled or not",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fleet Type",
                "verbose_name_plural": "Fleet Types",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="FormupLocation",
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
                        help_text="Short name to identify this formup location",
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
            ],
            options={
                "verbose_name": "Formup Location",
                "verbose_name_plural": "Formup Locations",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Webhook",
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
                    "type",
                    models.CharField(
                        choices=[("Discord", "Discord"), ("Slack", "Slack")],
                        default="Discord",
                        help_text="Is this a Discord or Slack webhook?",
                        max_length=7,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the channel this webhook posts to",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="URL of this webhook, e.g. https://discordapp.com/api/webhooks/123456/abcdef",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "is_embedded",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Whether this webhook's ping is embedded or not",
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        default=None,
                        help_text="You can add notes about this webhook here if you want",
                        null=True,
                    ),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Whether this webhook is active or not",
                    ),
                ),
                (
                    "restricted_to_group",
                    models.ManyToManyField(
                        help_text="Restrict ping right to this webhook to one or more groups.",
                        related_name="webhook_require_groups",
                        to="auth.Group",
                    ),
                ),
            ],
            options={
                "verbose_name": "Webhook",
                "verbose_name_plural": "Webhooks",
                "default_permissions": (),
            },
        ),
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