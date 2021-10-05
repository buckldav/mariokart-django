# Mario Kart API

---

Day 1

### Commands

#### Project Setup

```bash
python -m venv env
source env/Scripts/activate
pip install django
django-admin startproject <project-name> .
python manage.py runserver
```

#### Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

#### VS Code Extensions

Django
Draw.io Integration
Python

Ctrl+Shift+P >Python: Select Linter -> pylint

---

Day 2

#### Make an app

```bash
django-admin startapp <app-name>
```

#### Perform a migration

This takes our `models.py` to CREATE and ALTER TABLEs on the database

```bash
python manage.py makemigrations
python manage.py migrate
```

For the stats:
https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model

---

Day 3

pip freeze and git
json and serialization
drf?

Day 4

urls
drf-yasg
