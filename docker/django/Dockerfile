FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get install -y apt-transport-https


COPY ./django /srv/django
RUN /usr/local/bin/pip install -r /srv/django/requirements.txt --ignore-install


RUN ln -s /srv/django/manage.py /usr/local/bin/manage.py

EXPOSE 8000
WORKDIR /srv/django

COPY ./docker/django/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["manage.py", "runserver", "--verbosity=3", "0.0.0.0:8000"]
