FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code
# RUN mkdir /requirements
# WORKDIR /requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# Migrate
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown root:root /entrypoint.sh

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#RUN mkdir /code
#COPY . /code/
# List all files in the current directory
#RUN ls -la > /code/testSite/ls.txt