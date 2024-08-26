
FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 7000
CMD ["daphne", "-b", "0.0.0.0", "-p", "7002", "server1.asgi:application"]
