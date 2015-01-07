FROM rajalokan/dj_postgres

ADD requirements.pip /myproject/requirements.pip

WORKDIR /myproject

RUN /usr/local/bin/pip install -r requirements.pip

ENTRYPOINT ["/usr/bin/python", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

