FROM python:3.10.6-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
ENV PORT 8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT