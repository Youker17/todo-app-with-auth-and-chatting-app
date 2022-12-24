from channels.generic.websocket import WebsocketConsumer
import json
from asyncer import asyncify
from asgiref.sync import sync_to_async, async_to_sync
from . import models
from accounts.models import User

class Conversation(WebsocketConsumer):

    def connect(self):
        self.conversation = self.scope['path'].split('/')[-2]
        self.conversation_group_name = f"conv_id_{self.conversation}"
        
        async_to_sync(self.channel_layer.group_add)(
            self.conversation_group_name,
            self.channel_name
        )
        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.conversation_group_name,
            {
                "type":"connection_message",
                "content":f"connected !! group : {self.conversation_group_name}"
            }
        )
    def connection_message(self, data):
        msg = data["content"]
        self.send(text_data=json.dumps({"msg":msg,"type":"connection_message"}))
        
    
    
    # def disconnect(self, code):
    #     self.channel_layer.group_discard(
    #         self.conversation_group_name,
    #         self.channel_name
    #     )

    def receive(self, text_data):
        text_data_loaded = json.loads(text_data)
        # message = text_data_loaded["content"]
        print(text_data_loaded)
        content, owner=text_data_loaded["content"],text_data_loaded["sender"]
        print(content, owner)
        models.Message.objects.create(content=content, conv_id=int(self.scope['path'].split('/')[-2]), owner_id=owner)
        #  self.channel_layer.group_send(self.conversation_group_name,'saved')
        print("saved")
        self.sendtogrp(content, owner)
    def sendtogrp(self, content, owner):
        async_to_sync(self.channel_layer.group_send)(self.conversation_group_name,{'type':'chat_message',
                                                                                'message':content,
                                                                                'sender': owner,
                                                                                'status':'saved'})


    def chat_message(self, e):
        print(e)
        self.send(text_data=json.dumps(e))
        print('sent')


    