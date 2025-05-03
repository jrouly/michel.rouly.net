FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web web
COPY bin/start.sh bin/start.sh

ENTRYPOINT ["bin/start.sh"]
