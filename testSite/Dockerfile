FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code
# RUN mkdir /requirements
# WORKDIR /requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN chmod +x start.sh
CMD ["./start.sh"]

# Run server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]