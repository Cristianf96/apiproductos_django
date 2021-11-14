FROM python:3

COPY ["/ProductosAPI/", "/usr/src"]

WORKDIR /usr/src

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations", "api"]

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver"]