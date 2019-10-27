from sendSms import SmsQueue,ServiceProvider,SendSms
import unittest


class SmsService:
    """A service to send sms to service provider using  Sms Api: African Talking for thi case"""

    def __init__(self):
        self.smsq = SmsQueue()
        self.recipients = ServiceProvider()
        self.send = SendSms()
        """
        Create a new SmsService class that needs the below to work successfully
        1.messages : A queue of messages that will be send to service providers 
        2.recipients: A list of service providers that will receive this messages through their API endpoints
        """

    def send_sms(self):
        """sendSms is the function that send the smses to the service providers
        An instance(sending) of the class SendSms() is created to be able to access the function that it offers
        """
        sending =SendSms(add_recipient=False)
        """In the sending object, the dispatch method is capable of dispatching the messages to the service providers"""
        sending.dispatch()


if __name__ == '__main__':
    s = SmsService()
    s.send_sms()
    unittest.main()
