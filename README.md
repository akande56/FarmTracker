farmtracker ===========

[![Built with Cookiecutter React Django](https://img.shields.io/badge/built%20with-Cookiecutter%20React%20Django-blue)](https://img.shields.io/badge/built%20with-Cookiecutter%20React%20Django-blue)

## Local setup (on system)
ensure you download docker for your respective system, i.e windows or ubuntu. for ubuntu its simply through the terminal. i am not familiar with windows docker setup, but i know its in similar way in command prompt.

## (project docker setup)

On your terminal, simply do `docker-compose up --build`, and wait for the containers to build. Eventually, you'll be able to see the index page by going to `[0.0.0.0:8000]` for django api backend(this is simply for the api endpoint visualization) and `[http://172.20.0.3:3000/]` for react frontend.

for subsequent running of the container: `docker-compose up`
to run npm command on just the react container use: 


## Test coverage
To run the tests, check your test coverage, and generate a coverage report:

```
docker-compose run --rm django pytest
```



# read the doc2 file for current available endpoints that can be consumed in the react frontend
example of already consumed endpoint is at the homepage of react frontend that calculate lenght of entered characters


# to create a super user (admin account)
run `docker-compose run --rm django python3 manage.py createsuperuser`

access admin(developement purpose only....) backend practice UI: 0.0.0.0:8000/admin/  


## to install new packages on react container/frontend container 
run : `docker-compose run --rm react install <packageName>