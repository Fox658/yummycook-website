# syntax=docker/dockerfile:1
FROM python:3.6.4
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code

# install app dependencies
COPY requirements.txt /code/
RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . /code/
# install app

# final configuration
# ENV DJANGO_APP=hello
# EXPOSE 8000
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]
