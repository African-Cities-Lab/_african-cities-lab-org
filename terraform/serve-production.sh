# ssh-keygen -F github.com || ssh-keyscan github.com >> ~/.ssh/known_hosts
# git clone --single-branch -b staging git@github.com:martibosch/cookiecutter-django-terraform ~/app
cd /home/ubuntu/app
docker-compose -f production.yml run --rm django python manage.py migrate
docker-compose -f production.yml up --build -d
