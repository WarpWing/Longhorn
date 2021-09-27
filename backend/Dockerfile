FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
LABEL "repository"="https://github.com/WarpWing/Longhorn"
LABEL "maintainer"="Ty Chermsirivatana"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["uvicorn", "main:app", "--port", "5050"]
