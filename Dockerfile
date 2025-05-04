FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web web
COPY bin/start.sh bin/start.sh

RUN adduser --system --no-create-home nonroot
USER nonroot

EXPOSE 5000

ENTRYPOINT ["bin/start.sh"]
