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
            test case to check if user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

 
        
    
    def test_save_mutliple_users(self):
        '''
        test case for multiple users
        '''
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)   

    def test_delete_user(self):
        '''
        test case to see if we can delete a user
        '''
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)  

    def test_find_user(self):
        '''
        find a user through username
        '''
        self.new_user.save_user()
        test_user = User("user_name", "email", "password")
        test_user.save_user()
        self.find_user.test_user("email", "mzalendo23")  
        self.assertEqual(find_user.email, new_user.user_name)           

    if __name__ == "__main__":
     unittest.main()    