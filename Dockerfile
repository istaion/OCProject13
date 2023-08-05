FROM python:3.10.6-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
ENV PORT 8000
CMD python manage.py runserver 0.0.0.0:$PORT