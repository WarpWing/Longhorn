FROM python:3
LABEL "repository"="https://github.com/WarpWing/Longhorn"
LABEL "maintainer"="Ty Chermsirivatana"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
# This Container Logic is for injecting the data into Redis before the web app gets to retrieve it. This is so I don't have to hardcode existing data into the app.