# AA Discord Ping Formatter

[![Version](https://img.shields.io/pypi/v/aa-discord-ping-formatter?label=release)](https://pypi.org/project/aa-discord-ping-formatter/)
[![License](https://img.shields.io/badge/license-GPLv3-green)](https://pypi.org/project/aa-discord-ping-formatter/)
[![Python](https://img.shields.io/pypi/pyversions/aa-discord-ping-formatter)](https://pypi.org/project/aa-discord-ping-formatter/)
[![Django](https://img.shields.io/pypi/djversions/aa-discord-ping-formatter?label=django)](https://pypi.org/project/aa-discord-ping-formatter/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aa-discord-ping-formatter)](https://pypi.org/project/aa-discord-ping-formatter/)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)

App for formatting pings for Discord in Alliance Auth

## Archived

This app has been discontinued in favor of [AA Fleet Pings](https://github.com/ppfeufer/aa-fleetpings) and this Repository has been archived.

## Contents

- [Installation](#installation)
- [Updating](#updating)
- [Screenshots](#screenshots)
- [Configuration](#configuration)
- [Change Log](CHANGELOG.md)

## Installation

**Important**: This app is a plugin for Alliance Auth. If you don't have Alliance Auth running already, please install it first before proceeding. (see the official [AA installation guide](https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html) for details)

### Step 1 - Install app

Make sure you are in the virtual environment (venv) of your Alliance Auth installation. Then install the latest version:

```bash
pip install aa-discord-ping-formatter
```

### Step 2 - Update your AA settings

Configure your AA settings (`local.py`) as follows:

- Add `'discordpingformatter',` to `INSTALLED_APPS`


### Step 3 - Finalize the installation

Copy static files and run migrations

```bash
python manage.py collectstatic
```

```bash
python manage.py migrate
```

Restart your supervisor services for AA

### Step 4 - Setup permissions

Now you can setup permissions in Alliance Auth for your users. Add ``discordpingformatter | aa discord ping formatter | Can access this app`` to the states and/or groups you would like to have access.

## Updating

To update your existing installation of AA Discord Ping Formatter first enable your virtual environment.

Then run the following commands from your AA project directory (the one that contains `manage.py`).

```bash
pip install -U aa-discord-ping-formatter
```

```bash
python manage.py collectstatic
```

```bash
python manage.py migrate
```

Finally restart your AA supervisor services.

## Screenshots

### View in Alliance Auth

![AA View](https://raw.githubusercontent.com/ppfeufer/aa-discord-ping-formatter/master/discordpingformatter/docs/aa-view.jpg)

### Discord Ping

![Discord Ping Examples](https://raw.githubusercontent.com/ppfeufer/aa-discord-ping-formatter/master/discordpingformatter/docs/ping-examples.jpg)

_(Example for embedded ping (top) and non embedded ping (bottom))_

## Configuration

### Using Slack instead of Discord?

Don't worrie, I don't judge and you still can use this module. It supports also pings to Slack. Simply add the following to your `local.py`. 

```python
## AA Fleet Ping Formatter
AA_FLEETPINGFORMATTER_USE_SLACK = True
```

Although you cannot use your Auth groups as targets for pings with Slack.
