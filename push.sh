#!/bin/sh

pipenv run pip freeze > requirements.txt
git add .
git commit -m "$1"
ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa_private; git push origin'