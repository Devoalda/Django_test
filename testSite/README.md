# Test Django Project

## Installation from source

> Ensure that mariadb is installed and running

```bash
git clone https://github.com/Devoalda/Django_test.git
cd Django_test

python3 -m venv venv
source venv/bin/activate

cd testSite
pip install -r requirements.txt
cp env .env # Edit the .env file
```

## Run

```bash
python manage.py migrate
python manage.py runserver
```

Configure multiple instances with intellij run configurations and duplicate
the config with a different port number.

# Docker 

```
docker compose build
docker compose up -d
```

In another terminal
```bash
docker compose exec testsite # Go inside the container

python manage.py migrate
```

# Kubernetes
Install [Minikube](https://minikube.sigs.k8s.io/docs/start/), [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) and start minikube

```bash
minikube start
```

In another terminal:
```bash
cd k8s
kubectl apply -f .
```

## Migration

```bash
# Get minikube ip
minikube ip

# Get pod name
kubectl get pods

# Connect to the pod
kubectl exec -it <pod-name> -- python manage.py migrate

# Get service port
kubectl get services
```

## k8s endpoints

`http://<minikube-ip>:<service-port>/blog/` - List of api endpoints




# Endpoints

`http://127.0.0.1:8000/blog/` - List of api endpoints

`http://127.0.0.1:8000/blog/authors/` - Test multiple instance call (You should see duplicated data
with appended instance message)