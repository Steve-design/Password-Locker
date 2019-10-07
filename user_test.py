import unittest
from user import User
class TestUser(unittest,TestCase):

    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
 
        self.new_user = User("Steve Mwanza", "smzalendo31@gmail.com", "mzalendo") 

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []  

    def test_init(self):

            '''
            test_init test case for proper object initialization
            '''
            self.assertEqual(self.new_user.user_name,"Steve Mwanza")
            self.assertEqual(self.new_user.email,"smzalendo31@gmail.com")
            self.assertEqual(self.new_user.password,"mzalendo23")   

     def test_save_user(self):
        '''
            test case to test if new user  is saved into the contact list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

 
        #check whether you can store more than one user..............2
    
    def test_save_mutliple_users(self):
        '''
        test case to see if we can save multiple users.
        '''
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)        