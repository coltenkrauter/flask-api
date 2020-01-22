FROM python:3.7-alpine

# Update packages
RUN apk update 

# Install python3 libs and pip3
RUN apk add python3-dev libffi-dev libressl-dev openldap-dev

# Install a C/C++ compiler
RUN apk add gcc g++

# Add bash
RUN apk add --no-cache bash

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip \
&& pip3 install --upgrade setuptools

# Install certificates store
RUN apk add ca-certificates \
&& rm -rf /var/cache/apk/*

# Expose the flask port
EXPOSE 5000

# Set the Flask environment variable
ENV FLASK_ENV=production
ENV FLASK_APP=rest_api

# Install app dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# WSGI integration
COPY wsgi.py wsgi.py
COPY gunicorn.py gunicorn.py

# Bundle app source
COPY api/ api/

ENTRYPOINT ["gunicorn", "--preload", "--config", "gunicorn.py", "wsgi:app"]
