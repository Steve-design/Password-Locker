class User:

    user_list =[] 

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
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.user_name,"Steve Mwanza")
            self.assertEqual(self.new_user.email,"smzalendo31@gmail.com") #Check how initialisation happens as expected.
            self.assertEqual(self.new_user.password,"mzalendo23")      