FROM python:3.7

RUN pip install requests --index-url https://piwheels.org/simple

WORKDIR /var/app
