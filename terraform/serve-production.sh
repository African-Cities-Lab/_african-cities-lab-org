# ssh-keygen -F github.com || ssh-keyscan github.com >> ~/.ssh/known_hosts
# git clone --single-branch -b staging git@github.com:martibosch/cookiecutter-django-terraform ~/app
cd ~/app
docker-compose -f production.yml up --build -d
