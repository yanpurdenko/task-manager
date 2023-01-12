# Task Manager

Django project for IT companies for managing worker's tasks


# Check it out

...


## Installation

Python3 must be already installed

```shell
git clone https://github.com/YanPurdenko/task-manager
Set another DB in settings.py like this:
DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.sqlite3",
         "NAME": BASE_DIR / "db.sqlite3",
     }
 }  
cd task-manager
python3 -m venv venv
sourse venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## Features
- Authorization functionality for Workers/Users
- Change and reset password functionality
- Workers profile interface
- Updating profile functionality like changing avatar or edit some profile information
- Powerful admin panel for advanced managing
- And also create, update, delete, complete task functionality


## Demo

![Website Interface](demo.png)
