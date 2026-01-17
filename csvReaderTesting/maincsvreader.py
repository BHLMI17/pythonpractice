from testingtxt import alterCSV
# from account_system import Accounts
# from accountDB import AccountDB
import numpy as np
import pandas as pd

#important note, when running this main file, make sure you are in this directory, not the more external directory
#otherwise the csv file will not be found upon initialization

testingcsvfile = alterCSV("test1.csv")
# data = testingcsvfile.ReadCSV(5)
# print(data)

print(testingcsvfile.adjustNextAvailableID())