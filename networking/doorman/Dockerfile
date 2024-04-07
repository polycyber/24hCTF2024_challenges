FROM python:3-alpine

COPY app/ /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "/app/server.py", "0.0.0.0", "8998" ]