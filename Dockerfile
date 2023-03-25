FROM python:3.11.1-alpine
WORKDIR /usr/src/colourist
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install psycopg2
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# CMD ["gunicorn", "colourist.wsgi:application", "--bind", "0.0.0.0:8000"]
