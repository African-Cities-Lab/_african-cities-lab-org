# African Cities Lab

[![Build Status](https://github.com/African-Cities-Lab/african-cities-lab-org/workflows/CI/badge.svg?branch=main)](https://github.com/African-Cities-Lab/african-cities-lab-org/actions/workflows/ci.yml)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![GitHub license](https://img.shields.io/github/license/African-Cities-Lab/african-cities-lab-org.svg)](https://github.com/African-Cities-Lab/african-cities-lab-org/blob/main/LICENSE)

African Cities Lab website [africancitieslab.org](https://africancitieslab.org)

## Requirements

* docker
* docker-compose
* terraform

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
    # optionally add `-d` flag (or `--detach`) to run in detached mode
    docker-compose -f local.yml up --build
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

##### First-time setup

From the `terraform` directory, initalize terraform with the following command, which should only be run once (unless the provider/module versions change):

```bash
cd terraform
terraform init
```

Then, create a workspace for the `staging` and `production` environments by running the command below (which should only be run once):

```bash
terraform workspace new <env>  # replace `<env>` with the desired environment
```

##### Deployment

To deploy the changes, first select the desired environment (replace `<env>` accordingly in the commands below):

```bash
terraform workspace select <env>
```

Then, use the following command to see the planned changes:

```bash
terraform plan -var-file=<env>.tfvars \
    -var "do_token=${DO_PAT}" \
    -var "ssh_key_name=${DO_KEY_NAME}" \
    -var "spaces_access_id=${DO_ACCESS_ID}" \
    -var "spaces_secret_key=${DO_SECRET_KEY}"
```

and then apply them:

```bash
terraform apply -var-file=<env>.tfvars \
    -var "do_token=${DO_PAT}" \
    -var "ssh_key_name=${DO_KEY_NAME}" \
    -var "spaces_access_id=${DO_ACCESS_ID}" \
    -var "spaces_secret_key=${DO_SECRET_KEY}"
```


##### First-time wagtail steps

The following steps only need to be run once after the first deployment:

1. Go to the admin URL and and then to "Settings" > "Locales" and click "Add locale". Add the French locale and enable its synchronization from English.
2. Rename the default welcome page (in English) to "Home" (ensure that the slug is also updated to "home").
3. Create a French translation for the "Home" page, setting the title to "Accueil" and the slug to "accueil".
4. Create a News Index Page under the "Home" page, with "News" as title (and "news" as slug)
5. Create a French translation for the "News" page, setting the title to "Actualités" and the slug to "actualites".


## Acknowledgments

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)
