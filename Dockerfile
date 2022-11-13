# Dockerfile: blueprint for images, Image: Template for container, Container: actual running process

FROM --platform=arm64 python:3.11

ADD app.py .

COPY ./requirements.txt /var/code/requirements.txt
WORKDIR /var/code
RUN pip install -r requirements.txt

COPY ./run.sh /var/code/run.sh
RUN chmod a+x run.sh
CMD ["./run.sh"]

