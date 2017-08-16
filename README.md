# Seizure REST Service with SVM Analysis

Flask application that receives 4 parameters and says if the sent parameters correspond or not to a seizure.

## Run in dev mode

1. `cd webapp/`
1. `$> gunicorn wsgi --reload`

## Pushing to heroku

1. `heroku container:push web`

## License
MIT
