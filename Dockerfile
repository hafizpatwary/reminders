FROM python:3.6.8-slim

WORKDIR /opt/application
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
COPY application/ .