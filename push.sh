#!/bin/sh

git add .
git commit -m "$1"
pipenv run pip freeze > requirements.txt
ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa_private; git push origin'