class User:

    user_list =[] 

    user_list = []  
    def __init__(self, user_name, email, password):
        '''
        saving user credentials into user_list for login
        '''
        self.user_name = user_name
        self.email = email
        self.password = password
        
        
        
    def save_user(self):
        '''
        saving a user into our list of users
        '''
        User.user_list.append(self)



    def delete_user(self):
        '''
        delete a user from our list of users
        '''
        User.user_list.remove(self)
   

    def check_existing_user(self): 
        return User.check_existing_user(self) 


    def display_users(self):
	    '''
	    function that saves Users
	    '''
	    return User.display_users(self)     

    @classmethod
    def find_by_password(user_name, password):
        # '''
        # Method that takes in a name and returns a name that matches that user_name.

        # Args:
        #     name: password to search for
        # Returns :
        #     name of person that matches the name.
        # '''

        for user in cls.user_list:
            if user.user_name == User:
                return User