SHELL := /bin/bash
start:
	python manage.py runserver
migrate:
	python manage.py migrate
makemigrations:
	python manage.py makemigrations
venvact:
	source env.sh && /home/kirill/stationery-django/venv/bin/activate
venvdeact:
	deactivate
shell:
	python manage.py shell
