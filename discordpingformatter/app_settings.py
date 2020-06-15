from django.conf import settings
from .utils import clean_setting

# set default panels if none are set in local.py
AA_DISCORDFORMATTER_ADDITIONAL_PING_TARGETS = clean_setting('AA_DISCORDFORMATTER_ADDITIONAL_PING_TARGETS', [])
AA_DISCORDFORMATTER_ADDITIONAL_FLEET_TYPES = clean_setting('AA_DISCORDFORMATTER_ADDITIONAL_FLEET_TYPES', [])
