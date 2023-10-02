# Test Django Project

## Installation

> Ensure that mariadb is installed and running

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd testSite
cp env .env # Edit the .env file
```

## Docker 

```
docker compose build
docker compose up -d
```

In another terminal
```bash
python manage.py migrate
```

## Run

```bash
python manage.py migrate
python manage.py runserver
```

Configure multiple instances with intellij run configurations and duplicate
the config with a different port number.

## Endpoints

`http://127.0.0.1:8000/blog/` - List of api endpoints

`http://127.0.0.1:8000/blog/authors/` - Test multiple instance call (You should see duplicated data
with appended instance message)