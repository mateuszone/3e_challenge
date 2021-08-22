# Advertisement REST API

## Overview
#### Simple REST API which:
###### - read list of users by list method
###### - create new user in db (single record or multiple object inside list)
#### Because purpose of this app is very simple I've used a sqlite db, and uploaded it to github. Db is already filled with some random records. All steps related to the database are proactive, but not necessary to run the application 

### Technology:

##### Python 3.8

##### Djangorestframework 3.12.4

##### Django 3.2.6

# Installation

#### Create python3.8 venv

#### Install with pip:

`$ pip install -r requirements.txt`

#### Create db and make some migrations in terminal. 

`python3 manage.py migrate`

#### Create superuser to enter admin panel:

`python3 manage.py createsuperuser`

#### Run server:

`python3 manage.py runserver`

## Run API with Docker

##### In repository, you have files: Dockerfile and docker-compose.yml.


##### inside your project folder build docker and docker-up:

`sudo docker-compose build`

`sudo docker-compose up`

##### open another terminal window:

`sudo docker ps`

##### copy id of the container-id with web in name and type below command:

`sudo docker exec -it conteinerid bash`

##### Now you can use all drf and django commands
##### For example to populate db use:

`python3 manage.py migrate`

##### If you want to Stop sever go back to first terminal, click ctr + d and ctr + c and write:

`$ docker-compose down`


## API url's

#### Show list of available urls. By default, django runs at localhost http://127.0.0.1:8000/

### Users

##### This urls allow everyone to view list of users


`[GET] /users/`


### Users add
##### This url allow everyone to create (single or multiple) new user.

`[POST] /users/add/`


## Tests

#### To run simple test type in terminal:

`python manage.py test`