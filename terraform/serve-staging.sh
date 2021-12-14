# ssh-keygen -F github.com || ssh-keyscan github.com >> ~/.ssh/known_hosts
# git clone --single-branch -b staging git@github.com:martibosch/cookiecutter-django-terraform ~/app
cd ~/app
docker-compose -f production.yml -f production.staging.yml run --rm django python manage.py migrate
docker-compose -f production.yml -f production.staging.yml up --build -d
