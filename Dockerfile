FROM python:3.9.13-alpine3.16

WORKDIR /runner

RUN pip install -u pip 

RUN pip install requests

COPY . .

CMD ["sh", "entrypoint.sh"]
