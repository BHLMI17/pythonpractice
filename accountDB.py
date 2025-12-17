from account_system import Accounts

import numpy as np

#thinking this should be the area of the database where it could iterate through the values 
#so that new users can have unique ids

#perhaps i would need to have a class here for the database, so that it can work
class AccountDB:

    selectedAccount = None

    #trying to make it so that i can identify the type of data that the list is storing
    #but idk if its doing it automatically
    # accounts = Accounts[]
    accounts = []

    def __init__(self, accountList, chosenAccount):
        self.accounts = accountList
        self.selectedAccount = chosenAccount
        # self.selectedAccount = chosenAccount


    def returnSystem(self):
        return self.accounts
        

    # def storeAccount(self, selectedAccount = Accounts()):
    #     self.accounts.append(selectedAccount)
    #     #i want to set the index that the account rests in as the id for the account
    #     selectedAccount.account_id = self.accounts[selectedAccount]
    

    def storeAccount(self):
        self.accounts.append(self)


        #ok end product idea is to basically have an account added to the database 1 of 2 ways
        #storeAccount(each parameter) or storeAccount(accountname)
    


