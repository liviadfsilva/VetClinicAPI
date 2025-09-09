FROM python:3.11-slim

WORKDIR /vetclinicapi/vetclinic_project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .