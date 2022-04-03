import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(
            text_data=json.dumps(
                {
                    "type": "connection_established",
                    "message": "you are now connecte!",
                }
            )
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print("Message:\t", message)

        self.send(text_data=json.dumps({"type": "chat", "message": message}))
