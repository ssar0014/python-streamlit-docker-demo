# Dockerfile: blueprint for images, Image: Template for container, Container: actual running process

FROM FROM jupyter/scipy-notebook

EXPOSE 8501

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
CMD ["./run.sh"]
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

