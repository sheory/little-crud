# Little crud
This is a crud using flask and it's tools
- Flask
- flask_sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy


## How to run this project 

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True 

flask run
```

## How to migrate
```sh
flask db init
flask db migrate
flask db upgrade
```