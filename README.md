# African Cities Lab

[![Build Status](https://github.com/African-Cities-Lab/african-cities-lab-org/workflows/CI/badge.svg?branch=main)](https://github.com/African-Cities-Lab/african-cities-lab-org/actions/workflows/ci.yml)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![GitHub license](https://img.shields.io/github/license/African-Cities-Lab/african-cities-lab-org.svg)](https://github.com/African-Cities-Lab/african-cities-lab-org/blob/main/LICENSE)

African Cities Lab website [africancitieslab.org](https://africancitieslab.org)

## Requirements

* docker
* docker-compose
* ansible

## Development instructions

To set up a development environment, install the requirements and initialize pre-commit as follows:

```bash
pip install -r requirements/local.txt
pre-commit install
```

### Deployment instructions

This site is based on the [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) template, so further valuable information can also be found in [its documentation](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest).

#### Local deployment

1. Build the stack:

    ```bash
    docker-compose -f local.yml build
    docker-compose -f local.yml up
    ```

    alternatively, the above commands can be replaced by using the `deploy.local.yml` ansible playbook as in:

    ```bash
    ansible-playbook ansible/deploy.local.yml
    ```

2. Run the migrations:

    ```bash
    docker-compose -f local.yml run django python manage.py migrate
    ```

3. Create a super user:

    ```bash
    docker-compose -f local.yml run django python manage.py createsuperuser
    ```

#### Staging/production deployment

##### Server setup

In order to set up the staging and production servers, the following commands should be run once:

1. Create two computing server instances (e.g., AWS EC2, DigitalOcean droplet...), one for staging and another for production, and ensure that you have root ssh access rights to both (e.g., by running `ssh root@<server-ip>`).

2. Register a domain and create A DNS records to redirect the to the server IP addresses, e.g., create an A record mapping the base domain (e.g., "example.com") to the production server and another A record mapping a staging subdomain (e.g., "staging.example.com") to the staging server.

3. Execute the `ansible/setup.staging.yml` and `ansible/setup.production.yml` playbooks to setup the production and staging servers respectively:

    ```bash
    # ansible-playbook ansible/setup.staging.yml  # for staging
    ansible-playbook ansible/setup.production.yml  # for production
    ```

4. Create two storage bucket instances (e.g., AWS S3, DigitalOcean spaces...), one for staging and another for production.

5. Ensure that `.envs/.staging/.django` and `.envs/.production/.django` have the correct access keys for the staging and production storage buckets respectively.

##### Deployment

Once the servers are setup, you can push the latest commit to the main branch of this repository (https://github.com/African-Cities-Lab/african-cities-lab-org) and then deploy them to staging/production by executing the `ansible/deploy.staging.yml` and `ansible/deploy.production.yml` playbooks respectively:

```bash
# ansible-playbook ansible/deploy.staging.yml  # for staging
ansible-playbook ansible/deploy.production.yml  # for production
```

The web application should be now up and running in the staging and production servers

## Acknowledgments

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

* The ansible playbook of this repository is based on the approach of [rrebase/knboard](https://www.rrebase.com/posts/deploying-knboard-to-digitalocean-with-ansible).
