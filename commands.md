

## Run command inside docker container
```bash
docker-compose exec <docker-container> python manage.py <command>
```

## Start docker container in background
```bash
docker-compose up -d
```

## Start docker container that changed from last time
```bash
docker-compose up -d --no-deps --build <docker-container>
```

