class Credentials:
     credentials_list = [] 

     def __init__(self, account_name, login_detail , Password):
    
        self.account_name = account_name
        self.login_detail = login_detail
        self.Password = Password
        ''' 
        save our accounts passwords here.
        '''

     def save_credentials(self):
        Credentials.credentials_list.append(self) 
        '''
        functions that saves credentials once defined
        '''   

    
       