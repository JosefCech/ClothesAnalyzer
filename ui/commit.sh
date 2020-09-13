#!/bin/sh

pipenv run pip freeze > requirements.txt
ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa_private_josef ; git push origin docker '