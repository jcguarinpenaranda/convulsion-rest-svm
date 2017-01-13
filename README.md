# Miniconda on Heroku Example App

This repository contains two things:

- A `Dockerfile`.
- A Flask `webapp`, which utilizes basic functionality of `scikit-learn`.

## ☤ Advantages over [Conda Buildpack](https://github.com/kennethreitz/conda-buildpack):

- No slug size limit (Anaconda packages can be very large). 
- Exact Miniconda environment, from Continuum.

## ☤ Deploy this Application:

Deploy with the [Container Registry and Runtime](https://devcenter.heroku.com/articles/container-registry-and-runtime):

     $ heroku plugins:install heroku-container-registry
     $ heroku container:login
     
     $ git clone https://github.com/heroku-examples/python-miniconda
     $ cd python-miniconda
     
     $ heroku create
     $ heroku container:push 

✨🍰✨
