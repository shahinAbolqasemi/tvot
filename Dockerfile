FROM python:3.9.13-alpine3.16

WORKDIR /runner

RUN pip install -U pip 

RUN pip install requests
RUN pip install -U requests[socks]

COPY . .

CMD ["sh", "entrypoint.sh"]
