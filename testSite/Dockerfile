FROM python:3.10

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt /requirements/
RUN pip install -r requirements.txt --no-cache-dir

RUN mkdir /code
WORKDIR /code
COPY . /code/

# Run the application:
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]