FROM python:3.10
WORKDIR /django_example
COPY requirments.txt .
RUN pip install --upgrade pip && pip install -r requirments.txt
COPY . /django_example