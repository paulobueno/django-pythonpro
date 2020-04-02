# django-pythonpro
Django project created through Pythonpro classes

App available on:
* https://paulobdjango.herokuapp.com/
* https://django.pythonprojects.fun/

[![Python 3](https://pyup.io/repos/github/paulobueno/django-pythonpro/python-3-shield.svg)](https://pyup.io/repos/github/paulobueno/django-pythonpro/)
[![Build Status](https://travis-ci.org/paulobueno/django-pythonpro.svg?branch=master)](https://travis-ci.org/paulobueno/django-pythonpro)
[![Updates](https://pyup.io/repos/github/paulobueno/django-pythonpro/shield.svg)](https://pyup.io/repos/github/paulobueno/django-pythonpro/)

```
pip install pipenv
```
On .bashrc, add:  
```
export PIPENV_VENV_IN_PROJECT=1
alias mng='python $VIRTUAL_ENV/../manage.py'
```    
so your virtualenv will be created in your project's root and to create a shortcut `mng` so we can run django manage commands easily

To install all dependencies, including to develop, run the following command
```
pipenv install --dev
```
add your secret key to your `.env` file, that can be generated as bellow:
```
# on python terminal
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```

on terminal
```
mng migrate
```