import africastalking
from credentials import *


class SmsQueue:
    def __init__(self):
        self._messages = []

    def isEmpty(self):
        return self._messages == []

    def enqueue(self,sms):
        self._messages.insert(0,sms)

    def dequeue(self):
        self._messages.pop()

    def size(self):
        return len(self._messages)

    def printqueue(self):
        for sms in self._messages:
            print(sms)


class ServiceProvider:
    def __init__(self):
        self.providers = []

    def isEmpty(self):
        return self.providers == []

    def add_users(self):
        user = str(input("New provider? Add provider: "))
        self.providers.insert(0,user)
        return tuple(self.providers)

    def remove(self):
        self.providers.pop()

    def size(self):
        return len(self.providers)

    def printList(self):
        for sms in self.providers:
            print(sms)


class SendSms:
    def __init__(self,add_recipient=True):
        self.USERNAME = USERNAME # Authentications
        self.APIKEY = APIKEY
        self.messages = ['sms1','sms2','sms3','sms4','sms5']
        self.add_recipient = add_recipient
        self.recipient = ServiceProvider()

        # Initialize the SDK
        africastalking.initialize(self.USERNAME, self.APIKEY)
        # Get the SMS service
        self.sms = africastalking.SMS

    def dispatch(self):
        if self.recipient.isEmpty():
            """if the service provider list is empty, request for a number to be added so that the sms can be sent"""
            print("No user available to send sms")
            self.recipients = self.recipient.add_users()

        if self.add_recipient:
            # ask for a service provider's number if add_recipient boolean is set to True theb send sms'
            self.recipients = self.recipient.add_users()
            for recipient in self.recipients:
                user = recipient,
                for sms in self.messages:
                    response = self.sms.send(sms, user)
                    print(response)
        elif len(self.recipient.providers) < 0:
            print("No reciepients")
        else:
            for recipient in self.recipients:
                user = recipient,
                for sms in self.messages:
                    response = self.sms.send(sms, user)
                    print(response)
