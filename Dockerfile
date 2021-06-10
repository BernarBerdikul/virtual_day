# pull official base image
FROM python:3.9.4

# set work directory
WORKDIR /usr/src/app
RUN mkdir django_static
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./wsgi-entrypoint.sh .
RUN pip install -r requirements.txt

# copy project
COPY . .