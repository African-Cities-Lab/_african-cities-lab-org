# African Cities Lab

[![Build Status](https://github.com/martibosch/african-cities-lab-org/workflows/CI/badge.svg?branch=main)](https://github.com/martibosch/african-cities-lab-org/actions/workflows/ci.yml)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![GitHub license](https://img.shields.io/github/license/martibosch/african-cities-lab-org.svg)](https://github.com/martibosch/african-cities-lab-org/blob/main/LICENSE)

African Cities Lab website [africancitieslab.org](https://africancitieslab.org)

## Requirements

* docker
* docker-compose

## Deployment instructions

This site is based on the [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) template, so further valuable information can also be found in [its documentation](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest).

### Local deployment

1. Build the stack:

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up
```

2. Run the migrations:

```bash
docker-compose -f local.yml run django python manage.py migrate
```

3. Create a super user:

```bash
docker-compose -f local.yml run django python manage.py createsuperuser
```

## Development instructions

To set up a development environment, install the requirements and initialize pre-commit as follows:

```bash
pip install -r requirements/local.txt
pre-commit install
```

## Acknowledgments

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)
