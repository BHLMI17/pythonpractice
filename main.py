from room import Room
from testingtxt import alterCSV
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

# AccountDB.accountCreate()
# # print(AccountDB.accounts)
# print(AccountDB.returnSystem())

#initialize alterCSV class with the filename
csvfile = alterCSV("test1.csv")
# alterCSV.initialiseCSV()
# testcsv = alterCSV("test3.csv")
# testcsv.AppendCSV('simon','simon123')



# testcsv.initialiseCSV("simon")
# alterCSV.initialiseCSV("james")

# # #read first 5 rows from the csv file
# # data = csvfile.ReadCSV(5)
# # #print out the data read from the csv file
# # print(data)
# #ok lets now try to use my function to find the next available id
# # nextID = csvfile.determineNextAvailableID()
# # print(nextID)
# csvfile.AppendCSV('john', 'password123')
# csvfile.AppendCSV('james', 'james123')
# csvfile.AppendCSV('liamS', 'liam123')
csvfile.removeAccount()