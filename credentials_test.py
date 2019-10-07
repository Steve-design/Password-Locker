import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
     '''
    Test Class to test the behaviour of the credentials class
    '''
def setUp(self):    
        self.new_credentials = Credentials("Facebook", "0713519553", "mzalendo23")

def test_init(self):
        
            self.assertEqual(self.new_credentials.account_name, "Facebook",)
            self.assertEqual(self.new_credentials.login_detail, "0713519553")
            self.assertEqual(self.new_credentials.Password, "mzalendo23")
            '''
            confirms that initialisation of class Credentials happens as expected.Three parameters etc
            '''    
def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        '''
        confirms if cridentials can be saved
        '''

if __name__ == '__main__':
    unittest.main()            