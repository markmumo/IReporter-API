# IReporter-API

![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

# IReporter-API

iReporter is an app enables citizen to report any form of corruption.

## How it Works

-A user registers for an account

-A user then logs in

-A logged in user can report a red flag or request for a government intervention

-An admin then reviews the incident and can mark it as under investigation, resolved or rejected

-A user will then get notified with an sms or email regarding the marked status of the incident

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/markmumo/IReporter-API
```

### Create and activate a virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```bash
$ export FLASK_APP = run.py

$ export MODE = development

$ flask run
```

## Endpoints Available

### Testing

### Author

Mark Mumo
