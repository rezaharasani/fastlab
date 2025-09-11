FROM python:3.11.7-slim

WORKDIR /code

ENV TZ="Asia/Tehran"

RUN echo "$TZ" > /etc/timezone && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt-get update && \
    apt-get install -y --no-install-recommends tzdata && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ /code/

CMD ["fastapi", "run", "app/main.py"]

