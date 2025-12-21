from room import Room
from account_system import Accounts
from accountDB import AccountDB
import numpy as np
import pandas as pd
import sklearn as skl
# import dataframe as df




# room1 = Room(5, 2,4)
# print(room1.calculateVolume())
# print(room1.returnLength())
# print(room1.returnWidth())
# print(room1.returnHeight())

# print(room1.length)
# print(room1.width)
# print(room1.height)



# account1 = Accounts("bilal", "apple1")
# AccountDB.storeAccount(account1)
# print(AccountDB.accounts)

# account2 = Accounts("john", "smith2")
# AccountDB.storeAccount(account2)

AccountDB.accountCreate()
# print(AccountDB.accounts)
print(AccountDB.returnSystem())
