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
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []              
def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        '''
        confirms if cridentials can be saved
        '''
def test_saving_multiple_creds(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("LinkedIn", "mzalendo23.com","AmendTime23")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),4)
        '''
        Checks if saving multiple credentials is possible
        '''  

def test_delete_credentials(self): 
        self.new_credentials.save_credentials()
        test_credentials = Credentials("LinkedIn", "mzalendo23.com","AmendTime23")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1) 

def test_search_for_credentials(self):  
        self.new_credentials.save_credentials()
        test_credentials = Credentials("LinkedIn", "mzalendo23.com","AmendTime23")
        test_credentials.save_credentials()
        find_credentials= Credentials.find_account("Instagram")
        self.assertEqual(find_credentials.account_name, test_credentials.account )                     

if __name__ == '__main__':
    unittest.main()            