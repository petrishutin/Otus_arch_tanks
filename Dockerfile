FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /

COPY requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .




