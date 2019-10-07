import pyperclip
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
        function that saves credentials once defined
        '''   
     @classmethod
     def create_credentials(account_name, login_detail , Password):

        new_credentials = Credentials(account_name, login_detail , Password)
        return new_credentials   

     def delete_credentials(self):        
        Credentials.credentials_list.remove(self) 
        '''
        used to delete credentials 
        '''   

     @classmethod
     def find_account(cls, account_name):
        '''
        search for accounts
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials     