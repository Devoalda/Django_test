FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt /requirements/
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code
COPY . /code/

# Run the application:
RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8000