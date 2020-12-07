import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Test Data
up = {"uptime": "1"}
serverstat = {"OS": "Linux"}
x = {
   "Salt" : "2/3 Tablespoon",
   "Thyme" : "1/2 Tablespoon",
   "Basil" :  "1/2 Tablespoon",
   "Oregano" : "1/3 Tablespoon",
   "Celery Salt" : "1/3 Tablespoon",
   "Black Pepper": "1 Tablespoon",
   "Dry Mustard" : "1 Tablespoon", 
   "Paprika" : "3 Tablespoon", 
   "Garlic Salt" : "2 Tablespoon",
   "Ground Ginger" : "1 Tablespoon",
   "White Pepper" : "3 Tablespoon",
   "MSG" : "A LOT"
}


@app.route('/', methods=['GET'])
def home():
    return '''<p>Welcome to my prototype API Page </p>
<title> Longhorn API Test </title>
<p>There shouldn't be much to the frontend other than a few plain words. I would say that this should concern the backend more.</p>
<p>This API is now backed by a full CI/CD Pipeline! Check out the status of the pipeline <a href="https://github.com/WarpWing/Longhorn/actions" target="_blank" rel="noopener">here</a></p> </p>
<p>Check this API Endpoint for more information: /api/v1/</p>
<p>&nbsp;</p>
<p>This page was made by <a href="https://github.com/WarpWing/Longhorn" target="_blank" rel="noopener">WarpWing</a></p> 
'''

@app.route('/api/v1/', methods=['GET'])
def apiinfo():
    return '''<p>Welcome to the API v1 Endpoint </p>
<title> Longhorn API Test Endpoint v1</title>
<p>This is the API v1 Endpoint. You can get information outputted in JSON from the following endpoints </p>
<p>Uptime: v1/uptime</p>
<p>Server Statistics: v1/serverstats<p/>
<p>Health Check: v1/health<p/>
<p>This page was made by <a href="https://github.com/WarpWing/Longhorn" target="_blank" rel="noopener">WarpWing</a></p> 
''' 


@app.route('/api/v1/uptime', methods=['GET'])
def uptime():
    return jsonify(up) 

@app.route('/api/v1/serverstats', methods=['GET'])
def server_stats():
    return jsonify(serverstat) 

@app.route("/api/v1/health")
def health_check():
    status = {"status": "healthy"}
    if status['status'] != "healthy":
        return_code = 301
    else:
        return_code = 200
    return flask.jsonify(status), return_code

@app.route("/api/v1/kfc")
def kfc():
    return jsonify(x)

if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run(host='0.0.0.0')
