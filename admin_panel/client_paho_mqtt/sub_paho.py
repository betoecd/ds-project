import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

class Subscriber:

    def __init__(
        self, mqttbroker='test.mosquitto.org',
        user='administrator',
        topic='client_id',
    ):
        self.broker = mqttbroker
        self.user = user
        self.topic = topic

        self.client = mqtt.Client(self.user)
        self.client.connect(self.broker)
        self.client.loop_start()
        self.subscribe(self.topic)

    def loop_stop(self):
        return self.client.loop_stop()

# mqttBroker ="test.mosquitto.org"

# client = mqtt.Client("Administrator")
# client.connect(mqttBroker)

# client.loop_start()

# client.subscribe("TEMPERATURE")
# client.on_message=on_message

# client.loop_stop()
