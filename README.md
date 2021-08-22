# Advertisement REST API

## Overview
#### Simple REST API which:
## - read list of users by list method
## - create new user in db (single record or multiple object inside list)

### Technology:

##### Python 3.8

##### Djangorestframework 3.12.4

##### Django 3.2.6

# Installation

#### Create python3.8 venv

#### Install with pip:

`$ pip install -r requirements.txt`

#### Create db and make some migrations in terminal. If you will not use docker and want to use sqlite3 db just comment out current DATABASE settings with postgre in settings.py and uncomment DATABASE with sqlite3 settings. If you want to use postgres on local server you need to set up database settings in settings.py:

`python3 manage.py migrate`

#### Create superuser to enter admin panel:

`python3 manage.py createsuperuser`


## Run API with Docker

##### In repository, you have files: Dockerfile and docker-compose.yml.


##### inside your project folder build docker and docker-up:

`sudo docker-compose build`

`sudo docker-compose up`

##### open another terminal window:

`sudo docker ps`

##### copy id of the container-id with web in name and type below command:

`sudo docker exec -it conteinerid bash`

##### To populate db use:

`python3 manage.py migrate`

##### If you want to Stop sever:

`$ docker-compose down`


## API url's

#### Show list of available urls

### Users

##### These urls allow everyone to view list of users


`[GET] /users/`


### Users add
##### These url allow everyone to create (single or multiple) new user.

`[POST] /users/add/`


## Tests

#### To run simple test type in terminal:

`python manage.py test`