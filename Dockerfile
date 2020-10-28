FROM python:3
LABEL "repository"="https://github.com/WarpWing/APIPlayground"
LABEL "maintainer"="Ty Chermsirivatana"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "./main.py" ]