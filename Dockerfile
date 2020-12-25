FROM python:3
LABEL "repository"="https://github.com/WarpWing/Longhorn"
LABEL "maintainer"="Ty Chermsirivatana"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050"]
