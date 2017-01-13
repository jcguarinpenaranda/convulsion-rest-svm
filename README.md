# Miniconda on Heroku Example App

This repository contains two things:

- A `Dockerfile`
- A Flask `webapp`, which utilizes basic functionality of `scikit-learn`.

## Advantages over Conda Buildpack

- No slug size limit (Anaconda packages can be very large). 
- Exact Miniconda environment, from Continuum.

## Deploy this Application

     $ heroku plugins:install heroku-container-registry
     $ heroku container:login
     
     $ git clone https://github.com/heroku-examples/python-miniconda
     $ cd python-miniconda
     
     $ heroku create
     $ heroku container:push 

✨🍰✨
