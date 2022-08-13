import random
import time
import redis
import os

REDIS_HOST = os.getenv('REDIS_HOST')

def SendTelemetry():
    r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
    
    while True:
        latitude = random.uniform(-240, 240)
        longitude = random.uniform(-240, 240)
        altitude = random.uniform(-240, 240)
        
        MSG_TXT = '{{"latitude": {latitude}, "longitude": {longitude}, "altitude": {altitude}}}'
        
        msg_txt_formatted = MSG_TXT.format(latitude=latitude, longitude=longitude, altitude=altitude)
        
        print("{}".format(msg_txt_formatted))
        
        r.publish('my-channel-1', msg_txt_formatted)
        # client.send_message(msg_txt_formatted)
        print("Mensaje enviado con exito")
        time.sleep(1)

if __name__ == '__main__':
    SendTelemetry()