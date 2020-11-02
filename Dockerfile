From python:3

# upgrade pip
RUN pip install --upgrade pip

RUN mkdir -p /
WORKDIR /
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /

ENTRYPOINT behave