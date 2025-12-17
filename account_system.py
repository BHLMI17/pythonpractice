from accountDB import AccountDB
#so this is where i want the basic account system to be, how you can have a username, id and password,
#i can work on possible encryption later, but i need to link it to a database sometime soon of userIDs
#if i can create a list of accounts, that would be great, but for now, userIDs would suffice
class Accounts:
    #havent tested this out yet, think if im right, this will set the type and also set it to null
    account_id =  None
    account_username =  None
    account_password =  None


    def __init__(self, username, password):
        self.account_username = username
        self.account_password = password

    


    # def storeAccount(self):
    #     AccountDB.accounts.append(self)



        

        