import random, json, time
from producer import *
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config/app.properties')
TOPIC = app.config['PLANTS_TOPIC']
BOOTSTRAP_SERVERS = app.config['BOOTSTRAP_SERVERS']
SASL_USERNAME = app.config['KAFKA_SASL_USERNAME']
SASL_PASSWORD = app.config['KAFKA_SASL_PASSWORD']

def main():
    # create a config and producer instance
    config = ProducerConfig(topic=TOPIC, bootstrap_servers=BOOTSTRAP_SERVERS, username=SASL_USERNAME, password=SASL_PASSWORD)
    rp = Producer(config)

    # map topics to processors
    
    while (True):
        time.sleep(3)
        if keepRunning():
            no_msg_sent=random.randint(1, 5);
            print('Sending '+str(no_msg_sent)+' of message this time! ')
            for _ in range(no_msg_sent):
                bot_data = {    'plantId': random.randint(0, 100),    'botId':'B'+ str(random.randint(0, 100)),    'fulfillment': random.randint(2, 6)    }
                print(bot_data)
                rp.produce(key=str(bot_data['plantId']), message=bot_data)
            

def keepRunning():
    app.config.from_pyfile('config/app.properties')
    SWITCH=app.config['SWITCH']
    if(SWITCH=='ON'):
     return True
    
    return False

if __name__ == '__main__':
    main()