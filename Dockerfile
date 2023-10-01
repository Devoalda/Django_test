FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements.txt /requirements/
RUN pip install -r requirements.txt

RUN mkdir /code
COPY . /code/
WORKDIR /code/testSite
# List all files in the current directory
RUN ls -la > /code/testSite/ls.txt