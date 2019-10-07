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
    def find_user(cls, user_name, password):
        '''
        find user using search terms when logging in
        '''  
        
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password:
                verified_user = user
                return  verified_user