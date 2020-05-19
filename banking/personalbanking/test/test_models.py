from django.test import TestCase
# from banking.personalbanking import models
from personalbanking.models import Customer

class CustomerTestcases(TestCase):
    def setup(self):
        print('setup part')

    def test_login(self):
        print('testpart')
        response = self.client.get('/api/cust')
        print(response)
