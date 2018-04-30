# Taskboard

Yet another app for managing tasks

## Run

```
docker-compose -f docker-compose.yml up
```

## Run only server without database

```
pipenv install
pipenv shell
python3 manage.py runserver
```

## Build client

```
yarn
yarn dev
```