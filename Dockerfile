FROM python:3.9.2

ADD requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./app /app
WORKDIR /app
ENV PYTHONPATH=/app

ENTRYPOINT ["python","./super.py"]