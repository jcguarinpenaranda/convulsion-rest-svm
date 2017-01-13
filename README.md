# Miniconda Example Application

This repository contains two things:

- A `Dockerfile`
- A Flask `webapp`, which utilizes basic functionality of `scikit-learn`.

## Deploy this Application

     $ heroku plugins:install heroku-container-registry
     $ heroku container:login
     
     $ git clone https://github.com/heroku-examples/python-miniconda
     $ cd python-miniconda
     
     $ heroku create
     $ heroku container:push 

✨🍰✨