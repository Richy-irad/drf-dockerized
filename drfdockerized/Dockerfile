# use the official Python image from Docker Hub
FROM python:3.10-slim-bookworm

# Upgrade system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the working director in the container
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt /app/

# install the dependencies
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# copy the entire application into the container
COPY . /app/

# Run the django application in development mode
CMD ["python", "manage.py", "runserver", "0.0.0:8000"]
