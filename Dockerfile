FROM python:3.9
ENV PYTHONUNBUFFERED 1
EXPOSE 80
EXPOSE 443

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py runserver 0.0.0.0:8000
