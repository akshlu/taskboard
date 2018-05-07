# Taskboard

Yet another app for managing tasks

## Run

### For development (hot reload)
```
docker-compose -f docker-compose.dev.yml up
```

### For testing/production (build client and run server)
```
docker-compose -f docker-compose.prod.yml up
```

## Run only server without database

```
pipenv install
pipenv shell
python3 ./server/manage.py runserver
```

## Run client

```
cd ./client
yarn
yarn dev
```