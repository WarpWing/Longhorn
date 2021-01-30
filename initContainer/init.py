import redis 
import time 

print("Hello World! Initcontainer is here!")

cache = redis.Redis(host='0.0.0.0', port=6379) 

# Actual Backend Logic 
def add_redis(obj): # General increase or adding values to Redis objects and values. Must be a str.
    retries = 10
    while True:
        try:
            return cache.incr(obj)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def get_redis(obj): # General retriever function for getting Redis Objects and Values. Must be a str.
    retries = 10
    while True:
        try:
            return cache.get(obj)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)  

kfc = ''{"Salt" : "2/3 Tablespoon","Thyme" : "1/2 Tablespoon","Basil" :  "1/2 Tablespoon","Oregano" : "1/3 Tablespoon","Celery Salt" : "1/3 Tablespoon","Black Pepper": "1 Tablespoon","Dry Mustard" : "1 Tablespoon","Paprika" : "3 Tablespoon","Garlic Salt" : "2 Tablespoon","Ground Ginger" : "1 Tablespoon","White Pepper" : "3 Tablespoon"}''
add_redis(kfc)



print("Hello World! Initcontainer is finished!")