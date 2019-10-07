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