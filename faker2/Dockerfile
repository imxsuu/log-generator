FROM python:latest

ENV HOME=/home/

RUN apt-get update && apt-get install -y wget
RUN pip install Faker

WORKDIR .

COPY main.py .

CMD ["python3","main.py"]
