# Fleet management systems


## Local Development

### First Build Only
1. `cp .env.example .env`
2. `docker-compose up -d --build`

### Migrations
- Create Migrations
```shell
docker compose exec app python manage.py makemigrations
```
- Run migrations
```shell
docker compose exec app python manage.py migrate
```

### Load Base Data
```shell
docker compose exec app python manage.py load_menu_csv
```
```shell
docker compose exec app python manage.py load_struc_csv
```
```shell
docker compose exec app python manage.py load_service_tasks
```
```shell
docker compose exec app python manage.py load_auto_csv
```
```shell
docker compose exec app python manage.py load_changes_csv
```