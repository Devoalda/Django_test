# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Django (Hardcoded)
ENV DEBUG=True
ENV SECRET_KEY=your-secret-key
ENV DATABASE_URL=mysql://intellij:username:password@localhost:3306/databasename

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . .