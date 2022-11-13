# Dockerfile: blueprint for images, Image: Template for container, Container: actual running process

FROM --platform=arm64 python:3.11

EXPOSE 8501
USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN git clone https://github.com/ssar0014/python-streamlit-docker-demo.git .
RUN pip3 install -r requirements.txt

COPY ./run.sh .
RUN chmod a+x run.sh
RUN python3 dataset.py
RUN python3 train.py
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

