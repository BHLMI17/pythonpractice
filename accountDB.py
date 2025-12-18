from account_system import Accounts

import numpy as np

#thinking this should be the area of the database where it could iterate through the values 
#so that new users can have unique ids

#perhaps i would need to have a class here for the database, so that it can work
class AccountDB:


    #trying to make it so that i can identify the type of data that the list is storing
    #but idk if its doing it automatically
    # accounts = Accounts[]
    accounts = []

    

    #@classmethod makes it so that the method can be called on the class itself
    #instead of an instance of the class itself
    #uses cls instead of self for the first param
    @classmethod
    #so i will use AccountDB.storeAccount() to refer to the method here
    def storeAccount(cls, account: Accounts):
        #so instead of self, use cls to refer to the instance of the class
        account.account_id = len(cls.accounts)
        cls.accounts.append(account)


    @classmethod
    def returnSystem(cls):
        return cls.accounts
        

    
    

   


        #ok end product idea is to basically have an account added to the database 1 of 2 ways
        #storeAccount(each parameter) or storeAccount(accountname)
    


