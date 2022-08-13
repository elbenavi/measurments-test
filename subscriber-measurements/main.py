import redis
import time
import json
import requests
import os

REDIS_HOST = os.environ.get('REDIS_HOST')
MEASUREMENTS_HOST = os.environ.get('MEASUREMENTS_HOST')


r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

p = r.pubsub()
p.subscribe("my-channel-1")

url = f'{MEASUREMENTS_HOST}/api/v1/measurements'

print('Listen...')
while True:
    message = p.get_message()
    if message:
        if message.get('data') != 1:
            messageDict = json.loads( message.get('data').decode('utf-8') )
            x = requests.post(url, json = messageDict)
            print(messageDict)
    time.sleep(0.01)