FROM python:3-alpine3.8
LABEL "repository"="https://github.com/WarpWing/Longhorn"
LABEL "maintainer"="Ty Chermsirivatana"
WORKDIR /usr/src/app
COPY . . 
RUN pip3 install --no-cache-dir redis
CMD ["python3", "init.py"]
