#testing reading and writing onto a csv file
import csv
import pandas as pd
import os

class alterCSV:
    #ok so these lines allow you to write to a csv file, but i imagine if i change the mode to 'a' it will append instead of overwrite
    #similarly, changing mode to 'r' will allow reading
    # with open('testfile.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
    inputfile = None, csv

    
    def __init__(self, inputcsv):
        self.inputfile = inputcsv


    def ReadCSV(self, numberOfRows):
        with open(self.inputfile, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = []
            if self.determineNextAvailableID == 1:
                print("no rows in the csv file")
            for i, row in enumerate(reader):
                if i >= numberOfRows:
                    break
                rows.append(row)
        return rows
    

    def WriteCSV(self, username, password):
        with open(self.inputfile, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data = [self.determineNextAvailableID(), username, password]
            writer.writerow(data)

    #ok so apparently if you open it in 'a' mode it appends text to the end of the csv file
    def AppendCSV(self, username, password):
        with open(self.inputfile, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data = [self.determineNextAvailableID(), username, password]
            writer.writerow(data)







    def determineNextAvailableID(self):
        # If file doesn't exist or is empty, start at 1
        #wtf does the os library do?
        
        if not os.path.exists(self.inputfile) or os.path.getsize(self.inputfile) == 0:
            return 1

        df = pd.read_csv(self.inputfile)
        return len(df) + 1   
    


    #do i wanna focus on the encryption next or the security by making sure that multiple accounts can not have the same name 
    #it would be similar to a set in that regard
    #i could also work on the way to make sure that if you write on the csv, it ensures the header column is there, 
    #might be able to do that by making a refresh database method that just writes the column headers and nothing else        



            