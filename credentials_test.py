import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
     '''
    Test Class to test the behaviour of the credentials class
    '''
    def setUp(self):    
        self.new_credentials = Credentials("Facebook", "0713519553", "mzalendo23")

        