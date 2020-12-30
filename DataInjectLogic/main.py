import redis 
import json
#Redis Connection Set
cache = redis.Redis(host='0.0.0.0', port=6300)

# JSON Declaration 
KFC = {"Salt" : "2/3 Tablespoon","Thyme" : "1/2 Tablespoon","Basil" :  "1/2 Tablespoon","Oregano" : "1/3 Tablespoon","Celery Salt" : "1/3 Tablespoon","Black Pepper": "1 Tablespoon","Dry Mustard" : "1 Tablespoon","Paprika" : "3 Tablespoon","Garlic Salt" : "2 Tablespoon","Ground Ginger" : "1 Tablespoon","White Pepper" : "3 Tablespoon","MSG" : "1 Teaspoon"}

#JSON Injection
class JsonInject: 
    
    def __init__(self, target):
        self.target = target 

#JSON Test 
cache.execute_command('JSON.SET', 'object', '.', json.dumps(KFC))
reply = json.loads(cache.execute_command('JSON.GET', 'object'))
