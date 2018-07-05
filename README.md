# README #

Strona internetowa "Szpila" (deploy)

# Podstawowe zależności:

- Python 2.6 / 2.7 / 3.3
- Django 1.4 / 1.5 / 1.6
- Pillow
- grappelli-safe
- filebrowser-safe
- bleach and BeautifulSoup
- pytz and tzlocal
- South
- django-compressor
- requests and requests_oauthlib 
- pyflakes and pep8
- chardet
- fab

# Wirtualne środowisko do modyfikacji mezzanine (pierwsza instalacja):
 - instalacja pip:

    ``$ sudo apt-get install python-pip``

 - instalacja wirtualnego środowiska:

    ``$ sudo pip install virtualenvwrapper``

 - export:

    ``$ export WORKON_HOME=~/Envs``

 - tworzenie folderu roboczego:

    ``$ mkdir -p $WORKON_HOME``

 - ustawienie ścieżki:

    ``$ source /usr/local/bin/virtualenvwrapper.sh``

 - utworzenie wirtualnego środowiska:

    ``$ mkvirtualenv mezzanine``

 - instalacja bibliotek:

    ``$ pip install Django pep8 pyflakes``

 - instalacja projektu:

    ``$ pip install mezzanine``

 - przejście do folderu deweloperskiego:

    ``$ cd mezzanine``

 - uruchomienie skryptu paczek developerskich:

    ``$ python setup.py develop``

 - rosetta, compressor south:

    ``$ pip install django-rosetta django-compressor south``

 - kopiowanie szablonów prjektu-opcjonalnie:

    ``$ cp mezzanine/project_template/local_settings.py.template mezzanine/project_template/local_settings.py``

 - test składni-opcjonalnie:

    ``$ ./mezzanine/project_template/manage.py test``

#Obsługa wirtualnego środowiska:
    $ source /usr/local/bin/virtualenvwrapper.sh
    $ workon mezzanine
    $ python manage.py runserver
    http://127.0.0.1:8000

# Instalacja na serwerze (deploy):

Zdalny deploy:
- instalacja fabricate (na wirtualnym środowisku):

     $ pip install fabric

#Komendy:
- fab all - Installs everything required on a new system and deploy.
- fab apt - Installs one or more system packages via apt.
- fab backup - Backs up the database.
- fab create - Create a new virtual environment for a project.
- fab deploy - Deploy latest version of the project.
- fab install - Installs the base system and Python requirements for the entire server.
- fab manage - Runs a Django management command (e.g. fab manage: syncdb).
- fab pip - Installs one or more Python packages within the virtual environment.
- fab psql - Runs SQL against the project’s database.
- fab python - Runs Python code in the project’s virtual environment, with Django loaded.
- fab remove - Blow away the current project.
- fab restart - Restart gunicorn worker processes for the project.
- fab restore - Restores the database.
- fab rollback - Reverts project state to the last deploy.
- fab run - Runs a shell comand on the remote server.
- fab sudo - Runs a command as sudo.

#Obsługa South:
- python manage.py schemamigration [nazwa projektu np. project_template] --initial / --auto
- python manage.py migrate [nazwa projektu np. project_template]  / --fake

#Obsługa Rosetta:
- django-admin.py  makemessages -l pl