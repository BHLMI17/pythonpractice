from testingtxt import alterCSV
# from account_system import Accounts
# from accountDB import AccountDB
import numpy as np
import pandas as pd



testingcsvfile = alterCSV("test1.csv")
data = testingcsvfile.ReadCSV(5)
print(data)