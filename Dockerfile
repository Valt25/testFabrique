FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gettext && apt-get clean && \
    pip install uwsgi

WORKDIR /app

USER $MOD_WSGI_USER:$MOD_WSGI_GROUP

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD uwsgi --http :8000 --wsgi-file test_fabrique/wsgi.py
