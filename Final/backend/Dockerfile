FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

CMD ["gunicorn", "elearning.wsgi:application", "--bind", "0.0.0.0:8000"]
