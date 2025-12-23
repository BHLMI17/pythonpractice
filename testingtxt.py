#testing reading and writing onto a csv file
import csv
import pandas as pd

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





    def determineNextAvailableID(self):
        #use a try catch loop to make sure the error that the csv file is empty doesnt show up
        try:
            #read the csv file
            df = pd.read_csv(self.inputfile)
            if df.empty == False:
                return len(df) + 1             
        except pd.errors.EmptyDataError:

            return 1 



            