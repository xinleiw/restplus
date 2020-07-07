FROM hub.infervision.com/vendor/python:3.7.4-alpine3.10 as base
FROM base as builder

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories  && \
    apk add --update --no-cache build-base gcc linux-headers musl-dev zlib-dev jpeg-dev

RUN apk add --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone

ENV TZ Asia/Shanghai

COPY requirements.txt /app/
WORKDIR /app/

RUN pip install --upgrade pip  -i https://repos.infervision.com/repository/pypi/simple \
   && pip install -r /app/requirements.txt -i https://repos.infervision.com/repository/pypi/simple

COPY . /app

CMD ["circusd", "circus.ini"]
