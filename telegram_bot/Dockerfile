FROM python:3.11.7-alpine3.18

WORKDIR /app

# Устанавливаем необходимые пакеты для сборки
RUN apk update

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app
#COPY ./packages /app/packages

CMD ["python3", "app.py"]
