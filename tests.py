from sendSms import ServiceProvider
import unittest


class TestServiceProvider(unittest.TestCase):
    def setUp(self):
        self.recipient = ServiceProvider()

    def test_isEmpty_providers(self):
        self.assertEqual(self.recipient.isEmpty(),True, "service provider list is empty")

    def test_add_recipient(self):
        old_recipients = len(self.recipient.providers)
        new_recipients = len(self.recipient.add_users())
        self.assertGreater(new_recipients,old_recipients,"New list is greater")


class TestSendingSms(unittest.TestCase):
    def setUp(self):
        self.recipient = ServiceProvider()

